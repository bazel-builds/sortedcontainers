# sortedcontainers (Bazel build)

This repo vendors [grantjenks/python-sortedcontainers](https://github.com/grantjenks/python-sortedcontainers)
as a git subtree and adds Bazel build/test targets for it, so it can be
consumed as a Bazel dependency without relying on pip.

## Layout

- `sortedcontainers/` — upstream source, imported via `git subtree` at tag
  `v2.4.0`. Don't hand-edit files under here; see "Updating the vendored
  source" below.
- `BUILD` — Bazel targets for the library and its test suite.
- `MODULE.bazel` / `MODULE.bazel.lock` — bzlmod dependencies (`rules_python`,
  `rules_license`), the hermetic Python toolchain registration, and the
  `pip.parse` extension used to fetch `pytest` for tests.
- `requirements_lock.txt` — pinned, hashed `pytest` dependency used by the
  test target, generated with `uv pip compile`.
- `pytest_runner.py` — thin `py_test` entry point that hands off to
  `pytest.main`.
- `.bazelversion` — pins the Bazel version via [Bazelisk](https://github.com/bazelbuild/bazelisk).
- `.bazelrc` — build flags (see "Bootstrap flag" below).
- `LICENSE` — copied verbatim from `sortedcontainers/LICENSE` (Apache License
  2.0).

## Requirements

- [Bazelisk](https://github.com/bazelbuild/bazelisk) installed as `bazel` on
  your `PATH` (e.g. `brew install bazelisk`). Bazelisk reads `.bazelversion`
  and downloads the matching Bazel release automatically — no local Bazel
  install needed.

No local Python installation is required either: `MODULE.bazel` registers a
hermetic CPython 3.12 toolchain that Bazel downloads and uses for all builds
and tests, so results don't depend on whatever Python happens to be on your
machine.

## Building

```sh
bazel build //:sortedcontainers
```

## Testing

```sh
bazel test //:sortedcontainers_test
```

This runs upstream's `test_coverage_*.py` and `test_stress_*.py` suites
(297 tests) against the vendored source with `pytest`, using the hermetic
Python 3.12 toolchain. Upstream's `benchmark_*.py` and `plot_*.py` scripts
are not wired up as tests — they're developer tooling that depends on
optional third-party comparison libraries (`matplotlib`, `scipy`, `blist`,
etc.) that aren't needed to exercise the library itself.

## Bootstrap flag

`.bazelrc` sets:

```
build --@rules_python//python/config_settings:bootstrap_impl=script
```

`rules_python`'s default bootstrap (`system_python`) wires up `sys.path`
in-process without exporting `PYTHONPATH`, so tests that spawn a subprocess
can't find `sortedcontainers` in the child process. The legacy `script`
bootstrap sets `PYTHONPATH` as a real environment variable, which
subprocesses inherit.

## License metadata

The `//:license` and `//:package_info` targets declare this package's license
(Apache License 2.0 / SPDX `Apache-2.0`) using
[`rules_license`](https://github.com/bazelbuild/rules_license), and
`package(default_applicable_licenses = [":license"])` in `BUILD` attaches it
to every target in this package. This doesn't block "incompatible" licenses
on its own — it's metadata that a consumer's own compliance tooling can walk.
To see it, run `rules_license`'s aspect against a target, e.g.:

```sh
bazel build //:sortedcontainers \
  --aspects=@rules_license//rules:gather_licenses_info.bzl%gather_licenses_info_and_write \
  --output_groups=licenses
```

which writes a JSON manifest of the licenses used by that target's
transitive dependencies to `bazel-bin/sortedcontainers_licenses_info.json`.

## Updating the vendored source

To pull a newer release of `sortedcontainers`:

```sh
git subtree pull --prefix=sortedcontainers https://github.com/grantjenks/python-sortedcontainers.git <tag> --squash
```

Then re-run `bazel test //:sortedcontainers_test` and update `BUILD` if
upstream added/removed/renamed source or test files.

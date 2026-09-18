load("@rules_license//rules:license.bzl", "license")
load("@rules_license//rules:package_info.bzl", "package_info")
load("@rules_python//python:defs.bzl", "py_library", "py_test")

package(default_applicable_licenses = [":license"])

package_info(
    name = "package_info",
    package_name = "sortedcontainers",
    package_url = "https://github.com/grantjenks/python-sortedcontainers",
    package_version = "2.4.0",
)

license(
    name = "license",
    license_kinds = ["@rules_license//licenses/spdx:Apache-2.0"],
    package_name = "sortedcontainers",
)

py_library(
    name = "sortedcontainers",
    srcs = [
        "sortedcontainers/sortedcontainers/__init__.py",
        "sortedcontainers/sortedcontainers/sorteddict.py",
        "sortedcontainers/sortedcontainers/sortedlist.py",
        "sortedcontainers/sortedcontainers/sortedset.py",
    ],
    imports = ["sortedcontainers"],
    visibility = ["//visibility:public"],
)

py_test(
    name = "sortedcontainers_test",
    srcs = [
        "sortedcontainers/tests/__init__.py",
        "sortedcontainers/tests/context.py",
        "sortedcontainers/tests/test_coverage_sorteddict.py",
        "sortedcontainers/tests/test_coverage_sortedkeylist_modulo.py",
        "sortedcontainers/tests/test_coverage_sortedkeylist_negate.py",
        "sortedcontainers/tests/test_coverage_sortedlist.py",
        "sortedcontainers/tests/test_coverage_sortedset.py",
        "sortedcontainers/tests/test_stress_sorteddict.py",
        "sortedcontainers/tests/test_stress_sortedkeylist.py",
        "sortedcontainers/tests/test_stress_sortedlist.py",
        "sortedcontainers/tests/test_stress_sortedset.py",
        "pytest_runner.py",
    ],
    args = [
        "--import-mode=importlib",
    ],
    imports = ["sortedcontainers"],
    legacy_create_init = False,
    main = "pytest_runner.py",
    deps = [
        ":sortedcontainers",
        "@pip//pytest",
    ],
)

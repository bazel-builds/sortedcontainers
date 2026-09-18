import os
import sys

import pytest

if __name__ == "__main__":
    # Resolve the test directory relative to this file's own location in the
    # runfiles tree, not the workspace root: when this repo is vendored as a
    # git subtree into another Bazel workspace, this file (and the vendored
    # "sortedcontainers/tests" dir next to it) end up nested one level deeper
    # than the workspace root, so a hardcoded "sortedcontainers/tests" arg no
    # longer resolves.
    base = os.path.dirname(os.path.abspath(__file__))
    test_dir = os.path.join(base, "sortedcontainers", "tests")
    sys.exit(pytest.main([test_dir, *sys.argv[1:]]))

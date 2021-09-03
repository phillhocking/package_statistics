"""cli_test.py unit tests for package_statistics.py."""
import os
import subprocess
import sys

import pytest

cwd = os.getcwd()
print(cwd)


def test_entrypoint():
    """Test entry point exit 2 for usage."""
    exit_status = subprocess.call(cwd + "/package_statistics.py")
    assert exit_status == 2


def test_validarch():
    """Test with valid arch argument."""
    exit_status = subprocess.call([cwd + "/package_statistics.py", "amd64"])
    assert exit_status == 0

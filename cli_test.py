"""cli_test.py unit tests for package_statistics.py."""
import os
import subprocess
import sys

import pytest

cwd = subprocess.call("pwd", shell=True)
print(cwd)


def test_entrypoint():
    """Test entry point exit 2 for usage."""
    exit_status = subprocess.call("package_statistics")
    assert exit_status == 2


def test_validarch():
    """Test with valid arch argument."""
    exit_status = subprocess.call(["package_statistics", "amd64"])
    assert exit_status == 0

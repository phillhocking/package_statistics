"""cli_test.py unit tests for package_statistics.py."""
import pytest

import package_statistics


@pytest.fixture
def run(args):
    """Run package_statistics.py with arguments."""
    package_statistics.main(args)


run(amd64)
run(baz)

"""cli_test.py unit tests for package_statistics.py."""
import pytest
from cli_test_helpers import ArgvContext

import package_statistics


@patch("package_statistics.command.baz")
def test_cli_command(mock_command):
    """Verify the correct code called when invoked via the CLI."""
    with ArgvContext("baz"), pytest.raises(SystemExit):
        package_statistics()

    assert mock_command.called

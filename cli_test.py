"""tests.py unit tests for package_statistics.py."""
import pytest
from cli_test_helpers import ArgvContext

target = __import__("package_statistics.py")


@patch("package_statistics.command.amd64")
def test_cli_command(mock_command):
    """Verify the correct code called when invoked via the CLI."""
    with ArgvContext("arch", "amd64"), pytest.raises(SystemExit):
        package_statistics.package_statistics.main()

    assert mock_command.called

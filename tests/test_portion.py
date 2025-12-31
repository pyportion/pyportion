from unittest.mock import MagicMock
from unittest.mock import patch

from typer.testing import CliRunner

from portion.models import cli_state
from portion.portion import Portion

runner = CliRunner()


def test_help() -> None:
    app = Portion().cli
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0


def test_app_callback():
    app = Portion()

    assert cli_state.verbose is False
    assert cli_state.auto_confirm is False

    app.callback(verbose=True, auto_confirm=True)

    assert cli_state.verbose is True
    assert cli_state.auto_confirm is True


@patch("portion.portion.load_handlers")
def test_run(mock_load_handlers):
    p = Portion()
    p.cli = MagicMock()
    p.run()

    mock_load_handlers.assert_called_once_with(p.cli)
    p.cli.assert_called_once()

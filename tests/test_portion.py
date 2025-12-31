from typer.testing import CliRunner

from portion.models import cli_state
from portion.portion import Portion

runner = CliRunner()


def test_run() -> None:
    app = Portion().cli

    result = runner.invoke(app, [])
    assert result.exit_code == 2


def test_app_callback():
    app = Portion()

    assert cli_state.verbose is False
    assert cli_state.auto_confirm is False

    app.callback(verbose=True, auto_confirm=True)

    assert cli_state.verbose is True
    assert cli_state.auto_confirm is True

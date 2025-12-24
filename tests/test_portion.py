from typer.testing import CliRunner

from portion.portion import Portion


def test_run() -> None:
    runner = CliRunner()
    app = Portion().cli

    result = runner.invoke(app, [])
    assert result.exit_code == 2

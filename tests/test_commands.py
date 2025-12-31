import pytest
from typer.testing import CliRunner

from portion.portion import Portion
from portion.portion import load_handlers


@pytest.fixture
def app() -> Portion:
    app = Portion()
    load_handlers(app.cli)
    return app


def test_version_command(app):
    runner = CliRunner()
    result = runner.invoke(app.cli, ["version"])

    assert result.exit_code == 0
    assert "pyportion" in result.stdout.lower()

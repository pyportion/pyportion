import os

from typer.testing import CliRunner

from portion.models import Message
from portion.portion import Portion
from tests.utils import strip_ansi


def test_init_command_success(app: Portion) -> None:
    runner = CliRunner()

    with runner.isolated_filesystem():
        project_name = "test-project"
        result = runner.invoke(app.cli, ["init", project_name])

        assert result.exit_code == 0
        message = f"({project_name}) project has been initialized successfully"
        assert message == strip_ansi(result.stdout)
        assert os.path.exists(".pyportion.yml")


def test_init_command_project_already_initialized(app: Portion) -> None:
    runner = CliRunner()

    with runner.isolated_filesystem():
        project_name = "test-project"

        result = runner.invoke(app.cli, ["init", project_name])
        assert result.exit_code == 0
        assert Message.Init.PROJECT_EXIST not in result.stdout

        result = runner.invoke(app.cli, ["init", project_name])
        assert result.exit_code == 0
        assert Message.Init.PROJECT_EXIST in result.stdout

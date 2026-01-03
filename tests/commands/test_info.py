import os
from pathlib import PosixPath

from typer.testing import CliRunner

from portion.portion import Portion
from tests.utils import create_template
from tests.utils import create_template_with_portions


def test_info_command_no_project(app: Portion) -> None:
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(app.cli, ["info"])
        assert result.exit_code == 1


def test_info_command_with_project(mock_user_data_dir: PosixPath,
                                   app: Portion) -> None:
    runner = CliRunner()
    template_name = "cli-template"
    create_template(mock_user_data_dir, template_name)

    with runner.isolated_filesystem():
        project_name = "test-project"

        runner.invoke(app.cli, ["new", template_name, project_name])
        os.chdir(project_name)

        result = runner.invoke(app.cli, ["info"])
        assert result.exit_code == 0
        assert project_name in result.stdout
        assert template_name in result.stdout


def test_info_command_with_multiple_templates(mock_user_data_dir: PosixPath,
                                              app: Portion) -> None:
    runner = CliRunner()
    template1 = "cli-template"
    template2 = "web-template"
    create_template(mock_user_data_dir, template1)
    create_template_with_portions(mock_user_data_dir, template2)

    with runner.isolated_filesystem():
        project_name = "multi-template-project"

        runner.invoke(app.cli, ["new", template1, project_name])
        os.chdir(project_name)
        add_result = runner.invoke(app.cli, ["add", template2])
        assert add_result.exit_code == 0

        result = runner.invoke(app.cli, ["info"])
        assert result.exit_code == 0
        assert project_name in result.stdout
        assert template1 in result.stdout
        assert template2 in result.stdout


def test_info_command_displays_portions(mock_user_data_dir: PosixPath,
                                        app: Portion) -> None:
    runner = CliRunner()
    template_name = "template-with-portions"
    create_template_with_portions(mock_user_data_dir, template_name)

    with runner.isolated_filesystem():
        project_name = "test-project"

        runner.invoke(app.cli, ["new", template_name, project_name])
        os.chdir(project_name)

        result = runner.invoke(app.cli, ["info"])
        assert result.exit_code == 0
        assert template_name in result.stdout
        assert "A test template" in result.stdout
        assert "auth" in result.stdout
        assert "database" in result.stdout

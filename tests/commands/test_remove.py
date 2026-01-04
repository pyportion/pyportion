import os
from pathlib import PosixPath

from typer.testing import CliRunner

from portion.models import Message
from portion.portion import Portion
from tests.utils import create_template
from tests.utils import strip_ansi


def test_remove_command_no_project(app: Portion) -> None:
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(app.cli, ["remove", "some-template"])
        assert result.exit_code == 1


def test_remove_command_template_not_in_project(mock_user_data_dir: PosixPath,
                                                app: Portion) -> None:
    runner = CliRunner()
    template_name = "base-template"
    create_template(mock_user_data_dir, template_name)

    with runner.isolated_filesystem():
        project_name = "test-project"

        runner.invoke(app.cli, ["new", template_name, project_name])
        os.chdir(project_name)

        result = runner.invoke(app.cli, ["remove", "non-existent-template"])
        assert result.exit_code == 0
        assert Message.Remove.TEMPLATE_NOT_FOUND in result.stdout


def test_remove_command_success(mock_user_data_dir: PosixPath,
                                app: Portion) -> None:
    runner = CliRunner()
    base_template = "base-template"
    additional_template = "additional-template"
    create_template(mock_user_data_dir, base_template)
    create_template(mock_user_data_dir, additional_template)

    with runner.isolated_filesystem():
        project_name = "test-project"

        runner.invoke(app.cli, ["new", base_template, project_name])
        os.chdir(project_name)
        runner.invoke(app.cli, ["add", additional_template])

        result = runner.invoke(app.cli, ["remove", additional_template])
        assert result.exit_code == 0

        message = f"({additional_template}) has been removed successfully"
        assert message == strip_ansi(result.stdout)


def test_remove_command_after_multiple_adds(mock_user_data_dir: PosixPath,
                                            app: Portion) -> None:
    runner = CliRunner()
    base_template = "base-template"
    template1 = "template1"
    template2 = "template2"
    template3 = "template3"
    create_template(mock_user_data_dir, base_template)
    create_template(mock_user_data_dir, template1)
    create_template(mock_user_data_dir, template2)
    create_template(mock_user_data_dir, template3)

    with runner.isolated_filesystem():
        project_name = "test-project"

        runner.invoke(app.cli, ["new", base_template, project_name])
        os.chdir(project_name)
        runner.invoke(app.cli, ["add", template1])
        runner.invoke(app.cli, ["add", template2])
        runner.invoke(app.cli, ["add", template3])

        result = runner.invoke(app.cli, ["remove", template2])
        assert result.exit_code == 0
        message = f"({template2}) has been removed successfully"
        assert message == strip_ansi(result.stdout)


def test_remove_command_verify_with_info(mock_user_data_dir: PosixPath,
                                         app: Portion) -> None:
    runner = CliRunner()
    base_template = "base-template"
    additional_template = "additional-template"
    create_template(mock_user_data_dir, base_template)
    create_template(mock_user_data_dir, additional_template)

    with runner.isolated_filesystem():
        project_name = "test-project"

        runner.invoke(app.cli, ["new", base_template, project_name])
        os.chdir(project_name)
        runner.invoke(app.cli, ["add", additional_template])

        info_before = runner.invoke(app.cli, ["info"])
        assert additional_template in info_before.stdout

        runner.invoke(app.cli, ["remove", additional_template])

        info_after = runner.invoke(app.cli, ["info"])
        assert additional_template not in info_after.stdout

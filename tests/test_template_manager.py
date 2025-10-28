import os
from pathlib import PosixPath

import pytest

from portion.core.template_manager import TemplateManager


@pytest.fixture
def mock_user_data_dir(tmp_path: PosixPath,
                       monkeypatch: pytest.MonkeyPatch) -> PosixPath:
    monkeypatch.setattr("portion.core.template_manager.user_data_dir",
                        lambda: tmp_path)
    return tmp_path


def test_create_pyportion_dir(mock_user_data_dir: PosixPath) -> None:
    tm = TemplateManager()
    path = mock_user_data_dir / "pyportion"

    assert os.path.exists(path) is False
    tm.create_pyportion_dir()
    assert os.path.exists(path) is True


def test_download_template(mock_user_data_dir: PosixPath,
                           monkeypatch: pytest.MonkeyPatch) -> None:
    def mock_repo_clone(link, template_path) -> None:
        (mock_template_path).mkdir()

    tm = TemplateManager()
    template_name = "pyportion-template"
    mock_template_path = (mock_user_data_dir / "pyportion" / template_name)
    monkeypatch.setattr("portion.core.template_manager.Repo.clone_from",
                        mock_repo_clone)

    tm.create_pyportion_dir()
    assert (mock_template_path).exists() is False
    assert tm.is_template_exists(template_name) is False

    tm.download_template("pyportion.com")

    assert (mock_template_path).exists() is True
    assert tm.is_template_exists(template_name) is True


def test_delete_template(mock_user_data_dir: PosixPath) -> None:
    tm = TemplateManager()
    tm.create_pyportion_dir()
    template_name = "pyportion-template"

    assert tm.delete_template(template_name) is False

    template_path = (mock_user_data_dir / "pyportion" / template_name)
    template_path.mkdir()

    assert tm.delete_template(template_name) is True


def test_get_templates(mock_user_data_dir: PosixPath) -> None:
    tm = TemplateManager()
    tm.create_pyportion_dir()
    template_name = "pyportion-template"

    assert len(tm.get_templates()) == 0

    template_path = (mock_user_data_dir / "pyportion" / template_name)
    template_path.mkdir()

    templates = tm.get_templates()
    assert len(templates) == 1
    assert template_name in templates


def test_copy_template(mock_user_data_dir: PosixPath) -> None:
    tm = TemplateManager()
    tm.create_pyportion_dir()
    template_name = "pyportion-template"
    project_name = "pyportion-project"

    template_path = (mock_user_data_dir / "pyportion" / template_name)
    template_path.mkdir()

    pyportion_file_path = (template_path / ".pyportion.yml")
    pyportion_file_path.touch()

    project_path = (mock_user_data_dir / project_name)

    assert project_path.exists() is False
    tm.copy_template(template_name, str(project_path))
    assert project_path.exists() is True
    assert (project_path / ".pyportion.yml").exists() is True

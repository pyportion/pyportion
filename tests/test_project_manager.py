import os
from pathlib import PosixPath

from portion.core.project_manager import ProjectManager


pm = ProjectManager()


def test_is_project_exist(tmp_path: PosixPath) -> None:
    path = os.path.join(tmp_path, "project")
    assert pm.is_project_exist(path) is False


def test_create_project(tmp_path: PosixPath) -> None:
    path = os.path.join(tmp_path, "project")
    assert pm.is_project_exist(path) is False

    pm.create_project(path)
    assert pm.is_project_exist(path) is True

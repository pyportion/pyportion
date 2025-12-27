import os
from pathlib import PosixPath

from portion.core.project_manager import ProjectManager
from portion.models.project import ProjectTemplate
from portion.models.template import TemplateReplacements


pm = ProjectManager()


def test_is_project_exist(tmp_path: PosixPath) -> None:
    path = os.path.join(tmp_path, "project")
    assert pm.is_project_exist(path) is False


def test_create_project(tmp_path: PosixPath) -> None:
    path = os.path.join(tmp_path, "project")
    assert pm.is_project_exist(path) is False

    pm.create_project(path)
    assert pm.is_project_exist(path) is True


def test_initialize_project(tmp_path: PosixPath) -> None:
    path = os.path.join(tmp_path, "project")
    pm.create_project(path)

    assert pm.is_project_initalized(path) is False
    pm.initialize_project(path, "project")
    assert pm.is_project_initalized(path) is True


def test_replace_in_file(tmp_path: PosixPath) -> None:
    file_path = os.path.join(tmp_path, "test.txt")
    with open(file_path, "w") as f:
        f.write("Hello, {name}!")

    pm.replace_in_file(
        [str(tmp_path), "test.txt"],
        [TemplateReplacements(keyword="{name}",
                              value="World",
                              mode="uppercase")]
    )

    with open(file_path, "r") as f:
        content = f.read()
    assert content == "Hello, World!"


def test_read_configuration(tmp_path: PosixPath) -> None:
    path = os.path.join(tmp_path, "project")
    pm.create_project(path)
    pm.initialize_project(path, "project")

    config = pm.read_configuration(path)
    assert config.name == "project"
    assert config.templates == []


def test_update_configuration(tmp_path: PosixPath) -> None:
    path = os.path.join(tmp_path, "project")
    pm.create_project(path)
    pm.initialize_project(path, "project")

    config = pm.read_configuration(path)
    template = ProjectTemplate(name="temp",
                               link="https://github.com/pyportion/temp.git",
                               tag="v1.0.0")
    config.templates.append(template)

    pm.update_configuration(path, config)

    updated_config = pm.read_configuration(path)
    assert updated_config.templates == [template]

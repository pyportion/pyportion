import os
from pathlib import PosixPath

from rich.panel import Panel

from portion.core.project_manager import ProjectManager
from portion.models import PortionConfig
from portion.models import ProjectTemplate
from portion.models import TemplateConfig
from portion.models import TemplatePortion
from portion.models import TemplateReplacements

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


def test_get_project_info() -> None:
    config = PortionConfig(
        name="project",
        templates=[
            ProjectTemplate(name="temp1",
                            link="https://github.com/pyportion/temp1.git",
                            tag="v1.0.0"),
            ProjectTemplate(name="temp2",
                            link="https://github.com/pyportion/temp2.git",
                            tag="v1.0.0"),
            ProjectTemplate(name="temp3",
                            link="https://github.com/pyportion/temp3.git",
                            tag="v1.0.0"),
        ]
    )

    portions = [TemplatePortion(name=f"portion{i}", steps=[])
                for i in range(3)]

    templates_dict = {"temp1": TemplateConfig(name="temp1",
                                              version="1.0.0",
                                              description="Test Template",
                                              author="Author Name",
                                              type="cli",
                                              source=None,
                                              portions=portions),
                      "temp2": TemplateConfig(name="temp2",
                                              version="1.0.0",
                                              description="Another Template",
                                              author="Author Name",
                                              type="web",
                                              source=None,
                                              portions=[])
                      }

    panel = pm.get_project_info(config, templates_dict)
    assert isinstance(panel, Panel)

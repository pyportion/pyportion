from __future__ import annotations

import os
from pathlib import Path

from ruamel.yaml import YAML

from portion.models import Config
from portion.models import PortionConfig
from portion.models import TemplateReplacements


class ProjectManager:
    def __new__(cls) -> ProjectManager:
        if not hasattr(cls, "_instance"):
            cls._instance = super(cls, ProjectManager).__new__(cls)
        return cls._instance

    def is_project_exist(self, project_name: str) -> bool:
        return os.path.exists(project_name)

    def is_project_initalized(self, project_path: str | Path) -> bool:
        path = os.path.join(project_path, Config.portion_file)
        if os.path.exists(path):
            return True
        return False

    def create_project(self, project_name: str) -> None:
        os.mkdir(project_name)

    def initialize_project(self,
                           project_path: str | Path,
                           project_name: str) -> None:
        path = os.path.join(project_path, Config.portion_file)

        yaml = YAML()
        data = PortionConfig(name=project_name,
                             templates=[])

        with open(path, "w") as f:
            yaml.dump(data.model_dump(), f)

    def replace_in_file(self,
                        file_path: list[str],
                        replacements: list[TemplateReplacements]) -> None:
        with open(os.path.join(*file_path), "r+") as f:
            data = f.read()
            for replace in replacements:
                data = data.replace(replace.keyword, replace.value)
            f.seek(0)
            f.write(data)
            f.truncate()

    def read_configuration(self, project_path: str | Path) -> PortionConfig:
        path = os.path.join(project_path, Config.portion_file)
        yaml = YAML()

        with open(path, "r") as f:
            data = yaml.load(f)
        return PortionConfig(**data)

    def update_configuration(self,
                             project_path: str | Path,
                             config: PortionConfig) -> None:
        path = os.path.join(project_path, Config.portion_file)
        yaml = YAML()

        with open(path, "w") as f:
            yaml.dump(config.model_dump(), f)

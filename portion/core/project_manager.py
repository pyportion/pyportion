import os
from pathlib import Path

from ruamel.yaml import YAML

from portion.core.config import Config
from portion.models import PortionConfig


class ProjectManager:
    def is_project_exist(self, project_name: str) -> bool:
        return os.path.exists(project_name)

    def is_project_initalized(self, project_path: str | Path) -> bool:
        path = os.path.join(project_path, Config.PORTION_FILE)
        if os.path.exists(path):
            return True
        return False

    def create_project(self, project_name: str) -> None:
        os.mkdir(project_name)

    def initialize_project(self,
                           project_path: str | Path,
                           project_name: str) -> None:
        path = os.path.join(project_path, Config.PORTION_FILE)

        yaml = YAML()
        data = PortionConfig(name=project_name,
                             templates=[])

        with open(path, "w") as f:
            yaml.dump(data.model_dump(), f)

    def read_configuration(self, project_path: str | Path) -> PortionConfig:
        path = os.path.join(project_path, Config.PORTION_FILE)
        yaml = YAML()

        with open(path, "r") as f:
            data = yaml.load(f)
        return PortionConfig(**data)

    def update_configuration(self,
                             project_path: str | Path,
                             config: PortionConfig) -> None:
        path = os.path.join(project_path, Config.PORTION_FILE)
        yaml = YAML()

        with open(path, "w") as f:
            yaml.dump(config.model_dump(), f)

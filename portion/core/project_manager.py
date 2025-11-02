import os

from ruamel.yaml import YAML

from portion.core.config import Config
from portion.models import PortionMetadata


class ProjectManager:
    def is_project_exist(self, project_name: str) -> bool:
        return os.path.exists(project_name)

    def is_project_initalized(self, project_path: str) -> bool:
        path = os.path.join(project_path, Config.PORTION_FILE)
        if os.path.exists(path):
            return True
        return False

    def create_project(self, project_name: str) -> None:
        os.mkdir(project_name)

    def initialize_project(self, project_path: str, project_name: str) -> None:
        path = os.path.join(project_path, Config.PORTION_FILE)

        yaml = YAML()
        data = PortionMetadata(name=project_name,
                               portions=[])

        with open(path, "w") as f:
            yaml.dump(data.to_dict(), f)

import os

from ruamel.yaml import YAML

from portion.models import PortionMetadata

CONFIG_FILE = ".pyportion.yml"


class ProjectManager:
    def is_project_exist(self, project_name: str) -> bool:
        return os.path.exists(project_name)

    def create_project(self, project_name: str) -> None:
        os.mkdir(project_name)

    def initialize_project(self, project_name: str) -> None:
        yaml = YAML()
        data = PortionMetadata(name=project_name,
                               portions=[])

        with open(CONFIG_FILE, "w") as f:
            yaml.dump(data.to_dict(), f)

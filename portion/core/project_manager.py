import os
from dataclasses import asdict
from dataclasses import dataclass

from ruamel.yaml import YAML

CONFIG_FILE = ".pyportion.yml"


@dataclass
class Portion:
    name: str
    link: str
    tag: str


@dataclass
class PortionMetadata:
    name: str
    portions: list[Portion]


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
            yaml.dump(asdict(data), f)

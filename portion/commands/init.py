import sys

from portion.base import CommandBase
from portion.core import ProjectManager


class InitCommand(CommandBase):
    def __init__(self) -> None:
        super().__init__()
        self.project_manager = ProjectManager()

    def init(self, project_name: str) -> None:
        project_path = sys.path[0]

        if self.project_manager.is_project_initalized(project_path):
            self.logger.error("This project is already a portion project")
            return None

        self.project_manager.initialize_project(project_path, project_name)
        self.logger.info(f"The project {project_name} has "
                         "been initialized successfully")

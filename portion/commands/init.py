from pathlib import Path

from portion.base import CommandBase
from portion.core import ProjectManager


class InitCommand(CommandBase):
    def __init__(self) -> None:
        super().__init__()
        self.project_manager = ProjectManager()

    def init(self, project_name: str) -> None:
        path = Path.cwd()

        if self.project_manager.is_project_initalized(path):
            self.logger.error("This project is already a portion project")
            return None

        self.project_manager.initialize_project(path, project_name)
        self.logger.info(f"The project {project_name} has "
                         "been initialized successfully")

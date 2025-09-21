import os

from portion.base import CommandBase
from portion.core.logger import Logger


class NewCommand(CommandBase):
    def __init__(self,
                 name: str,
                 template: str,
                 logger: Logger) -> None:
        super().__init__(logger=logger)
        self.name = name
        self.template = template

    def is_project_exist(self) -> bool:
        return os.path.exists(self.name)

    def create_project(self) -> None:
        os.mkdir(self.name)

    def execute(self) -> None:
        self.logger.pulse("Executing create command")
        if self.is_project_exist():
            self.logger.error("The project is already exist")
            return None

        self.create_project()
        self.logger.pulse("Created the project folder")

        self.logger.info(f"{self.name} project has been created successfully")

import os

from platformdirs import user_data_dir
from git import Repo

from portion.base import CommandBase
from portion.core.logger import Logger


class TemplateCommand(CommandBase):
    def __init__(self,
                 template_command: str,
                 logger: Logger,
                 link: str | None = None) -> None:
        super().__init__(logger=logger)
        self.template_command = template_command
        self.link = link

        self._pyportion_path = os.path.join(user_data_dir(), "pyportion")

    def create_pyportion_dir(self) -> None:
        if not os.path.exists(self._pyportion_path):
            os.mkdir(self._pyportion_path)

    def download_command(self) -> None:
        if not self.link:
            raise ValueError("The given link is not valid")

        repo_name = self.link.split("/")[-1]
        repo_path = os.path.join(self._pyportion_path, repo_name)
        Repo.clone_from(self.link, repo_path)

    def execute(self) -> None:
        self.logger.pulse("Executing template command")

        self.create_pyportion_dir()

        if self.template_command == "download":
            self.download_command()

        self.logger.info("Done")

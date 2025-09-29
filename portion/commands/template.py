import os
import shutil

from platformdirs import user_data_dir
from git import Repo
from tabulate import tabulate

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
        portion_json_path = os.path.join(repo_path, "portion.json")

        self.logger.pulse(f"Clonning the template from {self.link}")
        Repo.clone_from(self.link, repo_path)
        if not os.path.exists(portion_json_path):
            shutil.rmtree(repo_path)
            self.logger.info("The given template is not a portion template")
            return None

        self.logger.info("Template is downloaded successfully")

    def list_command(self) -> None:
        headers = ["Template Name"]

        templates = [(x,)
                     for x in os.listdir(self._pyportion_path)
                     if not x.startswith(".")]

        table = tabulate(templates,
                         headers=headers,
                         tablefmt="simple_grid",
                         stralign="left",
                         numalign="center")
        self.logger.info(table)

    def execute(self) -> None:
        self.logger.pulse("Executing template command")

        self.create_pyportion_dir()

        commands = {
            "download": self.download_command,
            "list": self.list_command,
        }

        self.logger.pulse(f"Executing {self.template_command} sub-command")
        commands[self.template_command]()

        self.logger.pulse("Done executing template command")

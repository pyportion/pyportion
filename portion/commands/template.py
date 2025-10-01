from tabulate import tabulate

from portion.base import CommandBase
from portion.core import TemplateManager
from portion.core import Logger


class TemplateCommand(CommandBase):
    def __init__(self,
                 template_command: str,
                 logger: Logger,
                 link: str | None = None,
                 template_name: str | None = None) -> None:
        super().__init__(logger=logger)
        self.template_command = template_command
        self.link = link
        self.template_name = template_name

        self.template_manager = TemplateManager()

    def download_command(self) -> None:
        if not self.link:
            raise ValueError("The link is not valid")

        template_name = self.link.split("/")[-1]
        if self.template_manager.is_template_exists(template_name):
            self.logger.info("The given repo is already exist")
            return None

        self.logger.pulse(f"Clonning the template from {self.link}")
        self.template_manager.download_template(self.link)

        if self.template_manager.delete_if_not_template(template_name):
            self.logger.info("The given template is not a portion template")
            return None

        self.logger.info(f"{template_name} has downloaded successfully")

    def delete_command(self) -> None:
        if not self.template_name:
            raise ValueError("The template name is not valid")

        if self.template_manager.delete_template(self.template_name):
            self.logger.info(f"The {self.template_name} "
                             "has been deleted successfully")
            return None

        self.logger.info(f"The {self.template_name} template is not exist")

    def list_command(self) -> None:
        headers = ["Template Name"]
        templates = [(x,)
                     for x in self.template_manager.get_templates()
                     if not x.startswith(".")]

        if not templates:
            self.logger.info("There are no templates")
            return None

        table = tabulate(templates,
                         headers=headers,
                         tablefmt="simple_grid",
                         stralign="left",
                         numalign="center")
        self.logger.info(table)

    def execute(self) -> None:
        self.logger.pulse("Executing template command")

        self.template_manager.create_pyportion_dir()

        commands = {
            "download": self.download_command,
            "delete": self.delete_command,
            "list": self.list_command,
        }

        self.logger.pulse(f"Executing {self.template_command} sub-command")
        commands[self.template_command]()

        self.logger.pulse("Done executing template command")

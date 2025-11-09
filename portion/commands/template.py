from tabulate import tabulate

from portion.base import CommandBase
from portion.core import TemplateManager
from portion.models import TemplateSource


class TemplateCommand(CommandBase):
    def __init__(self) -> None:
        super().__init__()
        self.template_manager = TemplateManager()
        self.template_manager.create_pyportion_dir()

    def download(self, link: str) -> None:
        if not link:
            raise ValueError("The link is not valid")

        template_name = link.split("/")[-1]
        if self.template_manager.is_template_exists(template_name):
            self.logger.info("The given repo is already exist")
            return None

        self.template_manager.download_template(link)

        if self.template_manager.delete_if_not_template(template_name):
            self.logger.info("The given template is not a portion template")
            return None

        config = self.template_manager.read_configuration(template_name)
        config.source = TemplateSource(link=link, tag="main")
        self.template_manager.update_configuration(template_name, config)

        self.logger.info(f"{template_name} has downloaded successfully")

    def delete(self, template_name: str) -> None:
        if not template_name:
            raise ValueError("The template name is not valid")

        if self.template_manager.delete_template(template_name):
            self.logger.info(f"The {template_name} "
                             "has been deleted successfully")
            return None

        self.logger.info(f"The {template_name} template is not exist")

    def list(self) -> None:
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

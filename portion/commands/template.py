from tabulate import tabulate

from portion.base import CommandBase
from portion.core import Message
from portion.core import TemplateManager


class TemplateCommand(CommandBase):
    def __init__(self) -> None:
        super().__init__()
        self.template_manager = TemplateManager()
        self.template_manager.create_pyportion_dir()

    def download(self, link: str) -> None:
        if not link:
            raise ValueError(Message.Template.INVALID_LINK)

        template_name = link.split("/")[-1]
        if self.template_manager.is_template_exists(template_name):
            self.logger.error(Message.Template.TEMPLATE_EXIST)
            return None

        self.template_manager.download_template(link)

        if self.template_manager.delete_if_not_template(template_name):
            self.logger.error(Message.Template.NOT_PORTION_TEMPLATE)
            return None

        self.logger.info(Message.Template.DOWNLOADED,
                         template_name=template_name)

    def delete(self, template_name: str) -> None:
        if not template_name:
            raise ValueError(Message.Template.INVALID_NAME)

        if self.template_manager.delete_template(template_name):
            self.logger.info(Message.Template.TEMPLATE_DELETED,
                             template_name=template_name)
            return None

        self.logger.error(Message.Template.TEMPLATE_NOT_EXIST,
                          template_name=template_name)

    def list(self) -> None:
        headers = ["Template Name"]
        templates = [(x,)
                     for x in self.template_manager.get_templates()
                     if not x.startswith(".")]

        if not templates:
            self.logger.error(Message.Template.NO_TEMPLATES)
            return None

        table = tabulate(templates,
                         headers=headers,
                         tablefmt="simple_grid",
                         stralign="left",
                         numalign="center")
        self.logger.info(table)

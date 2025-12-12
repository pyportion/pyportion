import re

from tabulate import tabulate

from portion.base import CommandBase
from portion.core import TemplateManager
from portion.models import Config
from portion.models import Message


class TemplateCommand(CommandBase):
    def __init__(self) -> None:
        super().__init__()
        self.template_manager = TemplateManager()
        self.template_manager.create_pyportion_dir()

    def _check_link(self, link: str) -> bool:
        return bool(re.match(r"^https?:\/\/\S+$", link))

    def _resolve_link(self, link: str) -> str:
        if link.startswith("gh"):
            link = link.replace("gh", Config.github_base_url)
        elif link.startswith("gl"):
            link = link.replace("gl", Config.gitlab_base_url)
        return link

    def download(self, link: str) -> None:
        link = self._resolve_link(link)

        if not self._check_link(link):
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

    def remove(self, template_name: str) -> None:
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

    def info(self, template_name: str) -> None:
        config = self.template_manager.read_configuration(template_name)
        panel = self.template_manager.get_template_info(config)
        self.logger.print(panel)

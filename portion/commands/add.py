from pathlib import Path

from portion.base import CommandBase
from portion.core import ProjectManager
from portion.core import TemplateManager
from portion.models import ProjectTemplate


class AddCommand(CommandBase):
    def __init__(self) -> None:
        super().__init__()
        self.project_manager = ProjectManager()
        self.template_manager = TemplateManager()

    def add(self, template_name: str) -> None:
        if not self.template_manager.is_template_exists(template_name):
            self.logger.error("The given template is not exist")
            return None

        path = Path.cwd()
        pconfig = self.project_manager.read_configuration(path)

        for template in pconfig.templates:
            if template.name == template_name:
                self.logger.error("The template is already added")
                return None

        tconfig = self.template_manager.read_configuration(template_name)

        if not tconfig.source:
            self.logger.error("The template is incompelete")
            return None

        pconfig.templates.append(ProjectTemplate(name=tconfig.name,
                                                 link=tconfig.source.link,
                                                 tag=tconfig.source.tag))

        self.project_manager.update_configuration(path, pconfig)
        self.logger.info(f"{template_name} has been added successfully")

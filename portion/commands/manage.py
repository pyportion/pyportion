import sys

from portion.base import CommandBase
from portion.core import ProjectManager
from portion.core import TemplateManager
from portion.models import Template


class ManageCommand(CommandBase):
    def __init__(self) -> None:
        super().__init__()
        self.project_manager = ProjectManager()
        self.template_manager = TemplateManager()

    def add(self, template_name: str) -> None:
        if not self.template_manager.is_template_exists(template_name):
            self.logger.error("The given template is not exist")
            return None

        path = sys.path[0]
        config = self.project_manager.read_configuration(path)

        for template in config.templates:
            if template.name == template_name:
                self.logger.error("The template is already added")
                return None

        # TODO: template should be gotten from template manager
        config.templates.append(Template(name=template_name,
                                         link="",
                                         tag="v1.0.0"))

        self.project_manager.update_configuration(path, config)
        self.logger.info(f"{template_name} has been added successfully")

    def remove(self, template_name: str) -> None:
        path = sys.path[0]
        config = self.project_manager.read_configuration(path)

        for i, template in enumerate(config.templates):
            if template.name == template_name:
                config.templates.pop(i)
                break
        else:
            self.logger.error("The template isn't exist in this project")
            return None

        self.project_manager.update_configuration(path, config)
        self.logger.info(f"{template_name} has been removed successfully")

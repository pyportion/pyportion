from pathlib import Path

from portion.base import CommandBase
from portion.core import ProjectManager
from portion.core import TemplateManager


class RemoveCommand(CommandBase):
    def __init__(self) -> None:
        super().__init__()
        self.project_manager = ProjectManager()
        self.template_manager = TemplateManager()

    def remove(self, template_name: str) -> None:
        path = Path.cwd()
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

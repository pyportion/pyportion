import sys

from portion.base import CommandBase
from portion.core import ProjectManager
from portion.core import TemplateManager


class InstallCommand(CommandBase):
    def __init__(self) -> None:
        super().__init__()
        self.project_manager = ProjectManager()
        self.template_manager = TemplateManager()

    def install(self) -> None:
        path = sys.path[0]
        config = self.project_manager.read_configuration(path)

        for template in config.templates:
            try:
                self.template_manager.download_template(template.link)
                self.logger.info(f"{template.name} is successfully downloaded")
            except Exception:
                self.logger.error(f"Could not donwload {template.name}")

from portion.base import CommandBase
from portion.core import ProjectManager
from portion.core import TemplateManager


class BuildCommand(CommandBase):
    def __init__(self) -> None:
        super().__init__()
        self.project_manager = ProjectManager()
        self.template_manager = TemplateManager()

    def build(self) -> None:
        ...

import sys

from portion.base import CommandBase
from portion.core import ProjectManager
from portion.core import TemplateManager


class BuildCommand(CommandBase):
    def __init__(self) -> None:
        super().__init__()
        self.project_manager = ProjectManager()
        self.template_manager = TemplateManager()

    def build(self, portion_name: str) -> None:
        path = sys.path[0]

        pconfig = self.project_manager.read_configuration(path)

        tconfigs = [self.template_manager.read_configuration(x.name)
                    for x in pconfig.templates]

        portions = [x.portions for x in tconfigs]

        portions
        # search for command build
        # get the execution steps
        # execute them one by one

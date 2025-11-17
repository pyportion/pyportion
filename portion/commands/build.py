import sys

from portion.base import CommandBase
from portion.core import ProjectManager
from portion.core import TemplateManager
from portion.models import TemplateAskStep
from portion.models import TemplateCopyStep
from portion.models import TemplatePortion
from portion.models import TemplateReplaceStep


class BuildCommand(CommandBase):
    def __init__(self) -> None:
        super().__init__()
        self.project_manager = ProjectManager()
        self.template_manager = TemplateManager()
        self._memory: dict[str, str] = {}

    def _run_ask_step(self, step: TemplateAskStep) -> None:
        self.logger.info(step.question)
        self._memory[step.variable] = input()

    def _run_copy_step(self, step: TemplateCopyStep) -> None:
        print("Running Copy Step")

    def _run_replace_step(self, step: TemplateReplaceStep) -> None:
        print("Running Replace step")

    def _find_portion(self,
                      portions: list[TemplatePortion],
                      portion_name: str) -> TemplatePortion | None:
        for portion in portions:
            if portion.name == portion_name:
                return portion
        return None

    def build(self, portion_name: str) -> None:
        path = sys.path[0]

        pconfig = self.project_manager.read_configuration(path)

        portions = [portion
                    for x in pconfig.templates
                    for portion in
                    self.template_manager.read_configuration(x.name).portions]

        portion = self._find_portion(portions, portion_name)

        if not portion:
            self.logger.error(f"There is no portion called {portion_name}")
            return None

        for step in portion.steps:
            function = f"_run_{step.type.value}_step"
            getattr(self, function)(step)

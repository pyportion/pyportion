from pathlib import Path

from portion.base import CommandBase
from portion.core import ProjectManager
from portion.core import TemplateManager
from portion.models import ProjectTemplate
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

    def _run_ask_step(self,
                      template: ProjectTemplate,
                      step: TemplateAskStep) -> None:
        self.logger.info(step.question)
        self._memory[step.variable] = input()

    def _run_copy_step(self,
                       template: ProjectTemplate,
                       step: TemplateCopyStep) -> None:
        self.template_manager.copy_portion(template.name,
                                           step.from_path,
                                           step.to_path)

    def _run_replace_step(self,
                          Template: ProjectTemplate,
                          step: TemplateReplaceStep) -> None:
        print("Running Replace step")

    def _find_portion(self,
                      portions: list[tuple[ProjectTemplate, TemplatePortion]],
                      portion_name: str,
                      ) -> tuple[ProjectTemplate, TemplatePortion] | None:
        for template, portion in portions:
            if portion.name == portion_name:
                return template, portion
        return None

    def build(self, portion_name: str) -> None:
        path = Path.cwd()

        pconfig = self.project_manager.read_configuration(path)

        portions = [(t, portion)
                    for t in pconfig.templates
                    for portion in
                    self.template_manager.read_configuration(t.name).portions]

        template_portion = self._find_portion(portions, portion_name)

        if not template_portion:
            self.logger.error(f"There is no portion called {portion_name}")
            return None

        template, portion = template_portion

        for step in portion.steps:
            function = f"_run_{step.type.value}_step"
            getattr(self, function)(template, step)

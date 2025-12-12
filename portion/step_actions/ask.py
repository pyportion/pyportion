from portion.base import ActionBase
from portion.core import Logger
from portion.models import ProjectTemplate
from portion.models import TemplateAskStep


class AskAction(ActionBase[TemplateAskStep]):
    def __init__(self,
                 step: TemplateAskStep,
                 project_template: ProjectTemplate,
                 memory: dict[str, str],
                 logger: Logger) -> None:
        super().__init__(step, project_template, memory, logger)

    def prepare(self) -> None:
        return None

    def apply(self) -> None:
        self.logger.info(self.step.question)
        answer = input()
        self.memory[self.step.variable] = answer

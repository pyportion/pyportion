from portion.base import ActionBase
from portion.core import Logger
from portion.models import ProjectTemplate
from portion.models import TemplatePortionStepsType

from .ask import AskAction
from .copy import CopyAction
from .replace import ReplaceAction

all_actions = {
    "ask": AskAction,
    "copy": CopyAction,
    "replace": ReplaceAction,
}


def create_action(step: TemplatePortionStepsType,
                  project_template: ProjectTemplate,
                  memory: dict[str, str],
                  logger: Logger) -> ActionBase:
    return all_actions[step.type.value](step, project_template, memory, logger)

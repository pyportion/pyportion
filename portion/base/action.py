from typing import Generic
from typing import TypeVar

from portion.core import Logger
from portion.models import ProjectTemplate

TStep = TypeVar("TStep")


class ActionBase(Generic[TStep]):
    def __init__(self,
                 step: TStep,
                 project_template: ProjectTemplate,
                 memory: dict[str, str],
                 logger: Logger) -> None:
        self.step = step
        self.project_template = project_template
        self.memory = memory
        self.logger = logger

    def prepare(self) -> None:
        raise NotImplementedError()

    def apply(self) -> None:
        raise NotImplementedError()

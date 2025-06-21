from abc import ABC
from abc import abstractmethod

from portion.core import Logger


class CommandBase(ABC):
    def __init__(self, logger: Logger, **kwargs: dict) -> None:
        self.logger = logger

    @abstractmethod
    def execute(self) -> None:
        raise NotImplementedError()

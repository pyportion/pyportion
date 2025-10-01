from typing import Dict

from abc import ABC
from abc import abstractmethod

from portion.core import Logger


class CommandBase(ABC):
    def __init__(self, logger: Logger, **kwargs: Dict[str, str]) -> None:
        self.logger = logger

    @abstractmethod
    def execute(self) -> None:
        raise NotImplementedError()

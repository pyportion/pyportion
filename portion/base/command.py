from abc import ABC
from abc import abstractmethod


class CommandBase(ABC):
    def __init__(self, *args, **kwargs) -> None:
        ...

    @abstractmethod
    def execute(self) -> None:
        raise NotImplementedError()

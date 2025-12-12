from importlib.metadata import version

from portion.base import CommandBase
from portion.models import Message


class VersionCommand(CommandBase):
    def __init__(self) -> None:
        super().__init__()

    def version(self) -> None:
        self.logger.info(Message.Version.DISPLAY,
                         version=version("pyportion"))

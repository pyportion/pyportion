from portion.base import CommandBase
from portion.core.logger import Logger


class CreateCommand(CommandBase):
    def __init__(self, logger: Logger) -> None:
        self.logger = logger

    def execute(self) -> None:
        self.logger.pulse("Executing create command")
        self.logger.info("Done")

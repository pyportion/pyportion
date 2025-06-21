from portion.base import CommandBase
from portion.core.logger import Logger


class AddCommand(CommandBase):
    def __init__(self, logger: Logger) -> None:
        super().__init__(logger=logger)

    def execute(self) -> None:
        self.logger.pulse("Executing add command")
        self.logger.info("Done")

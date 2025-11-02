from importlib.metadata import version

from portion.base import CommandBase


class VersionCommand(CommandBase):
    def __init__(self) -> None:
        super().__init__()

    def version(self) -> None:
        self.logger.info(f"PyPortion: {version('pyportion')}")

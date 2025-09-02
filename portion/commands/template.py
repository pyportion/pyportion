from portion.base import CommandBase
from portion.core.logger import Logger


class TemplateCommand(CommandBase):
    def __init__(self,
                 template_name: str,
                 repo_url: str,
                 logger: Logger) -> None:
        super().__init__(logger=logger)
        self.template_name = template_name
        self.repo_url = repo_url

    def execute(self) -> None:
        self.logger.pulse("Executing template command")
        self.logger.info("Done")

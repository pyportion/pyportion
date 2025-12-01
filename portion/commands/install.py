from pathlib import Path

from portion.base import CommandBase
from portion.core import ProjectManager
from portion.core import TemplateManager
from portion.core.message import Message


class InstallCommand(CommandBase):
    def __init__(self) -> None:
        super().__init__()
        self.project_manager = ProjectManager()
        self.template_manager = TemplateManager()

    def install(self) -> None:
        path = Path.cwd()

        self.logger.pulse(Message.Install.READING_CONFIGURATION)
        config = self.project_manager.read_configuration(path)

        for template in config.templates:
            try:
                self.logger.pulse(Message.Install.DOWNLOADING_TEMPALTE,
                                  template_name=template.name,
                                  template_link=template.link)

                self.template_manager.download_template(template.link)

                self.logger.info(Message.Install.DOWNLOADED,
                                 template_name=template.name)

            except Exception:
                self.logger.error(Message.Install.COULD_NOT_DOWNLOAD,
                                  template_name=template.name)

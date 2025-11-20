from portion.base import CommandBase
from portion.core import ProjectManager
from portion.core import TemplateManager
from portion.models import ProjectTemplate


class NewCommand(CommandBase):
    def __init__(self) -> None:
        super().__init__()
        self.project_manager = ProjectManager()
        self.template_manager = TemplateManager()

    def new(self, template_name: str, project_name: str) -> None:
        if self.project_manager.is_project_exist(project_name):
            self.logger.error("The project is already exist")
            return None

        if not self.template_manager.is_template_exists(template_name):
            self.logger.error("The template is not exist")
            return None

        tconfig = self.template_manager.read_configuration(template_name)

        if not tconfig.source:
            self.logger.error("The template is incompelete")
            return None

        self.project_manager.create_project(project_name)
        self.template_manager.copy_template(template_name, project_name)
        self.project_manager.initialize_project(project_name, project_name)

        pconfig = self.project_manager.read_configuration(project_name)
        pconfig.templates.append(ProjectTemplate(name=tconfig.name,
                                                 link=tconfig.source.link,
                                                 tag=tconfig.source.tag))
        self.project_manager.update_configuration(project_name, pconfig)

        self.logger.info(f"{project_name} project is successfully created")

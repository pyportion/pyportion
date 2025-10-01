import os


class ProjectManager:
    def is_project_exist(self, project_name: str) -> bool:
        return os.path.exists(project_name)

    def create_project(self, project_name: str) -> None:
        os.mkdir(project_name)

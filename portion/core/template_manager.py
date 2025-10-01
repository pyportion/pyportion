import sys
import os
import shutil

from git import Repo
from platformdirs import user_data_dir


class TemplateManager:
    def __init__(self) -> None:
        self._pyportion_path = os.path.join(user_data_dir(), "pyportion")

    def create_pyportion_dir(self) -> None:
        if not os.path.exists(self._pyportion_path):
            os.mkdir(self._pyportion_path)

    def is_template_exists(self, template_name: str) -> bool:
        template_path = os.path.join(self._pyportion_path, template_name)
        return os.path.exists(template_path)

    def download_template(self, link: str) -> bool:
        template_name = link.split("/")[-1]
        template_path = os.path.join(self._pyportion_path, template_name)
        try:
            Repo.clone_from(link, template_path)
            return True
        except Exception:
            return False

    def delete_if_not_template(self, template_name: str) -> bool:
        template_path = os.path.join(self._pyportion_path, template_name)
        portion_json_path = os.path.join(template_path, "portion.json")
        if not os.path.exists(portion_json_path):
            shutil.rmtree(template_path)
            return True
        return False

    def delete_template(self, template_name: str) -> bool:
        template_path = os.path.join(self._pyportion_path,
                                     template_name)

        if os.path.exists(template_path):
            shutil.rmtree(template_path)
            return True
        return False

    def get_templates(self) -> list[str]:
        return os.listdir(self._pyportion_path)

    def copy_template(self, template_name: str, project_name: str) -> None:
        template_path = os.path.join(self._pyportion_path,
                                     template_name)

        project_path = os.path.join(sys.path[0], project_name)

        shutil.copytree(src=template_path,
                        dst=project_path,
                        dirs_exist_ok=True)

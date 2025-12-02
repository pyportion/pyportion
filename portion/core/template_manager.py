import os
import shutil

from git import Repo
from platformdirs import user_data_dir
from ruamel.yaml import YAML

from portion.models import Config
from portion.models import TemplateConfig


class TemplateManager:
    def __init__(self) -> None:
        self._pyportion_path = os.path.join(user_data_dir(),
                                            Config.portion_dir)

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
        portion_json_path = os.path.join(template_path,
                                         Config.portion_file)
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
                                     template_name,
                                     "base")

        shutil.copytree(src=template_path,
                        dst=project_name,
                        dirs_exist_ok=True)

    def copy_portion(self,
                     template_name: str,
                     portion_path: list[str],
                     dest_path: list[str]) -> None:

        path = os.path.join(self._pyportion_path,
                            template_name,
                            ".portion",
                            *portion_path)

        dest = os.path.join(*dest_path)
        shutil.copyfile(path, dest)

    def read_configuration(self, template_name: str) -> TemplateConfig:
        path = os.path.join(self._pyportion_path,
                            template_name,
                            Config.portion_file)

        yaml = YAML()
        with open(path, "r") as f:
            data = yaml.load(f)
        return TemplateConfig(**data)

    def update_configuration(self,
                             template_name: str,
                             config: TemplateConfig) -> None:
        path = os.path.join(self._pyportion_path,
                            template_name,
                            Config.portion_file)

        yaml = YAML()
        with open(path, "w") as f:
            yaml.dump(config.model_dump(), f)

from pathlib import PosixPath

from portion.core import TemplateManager


def create_template(mock_user_data_dir: PosixPath,
                    template_name: str) -> None:
    tm = TemplateManager()
    tm.create_pyportion_dir()

    template_path = mock_user_data_dir / "pyportion" / template_name
    template_path.mkdir(parents=True)
    base_path = template_path / "base"
    base_path.mkdir()

    config_str = f"""\
      name: {template_name}
      version: 1.0.0
      description: A test template
      author: Test Author
      type: test
      source:
        link: https://github.com/test/template
        tag: v1.0.0
      """
    config_file = template_path / ".pyportion.yml"
    config_file.write_text(config_str)
    (base_path / ".pyportion.yml").touch()


def create_template_with_portions(mock_user_data_dir: PosixPath,
                                  template_name: str) -> None:
    """Helper function to create a template with portions."""
    tm = TemplateManager()
    tm.create_pyportion_dir()

    template_path = mock_user_data_dir / "pyportion" / template_name
    template_path.mkdir(parents=True)
    base_path = template_path / "base"
    base_path.mkdir()

    config_str = f"""\
      name: {template_name}
      version: 1.0.0
      description: A test template with portions
      author: Test Author
      type: test
      source:
        link: https://github.com/test/template
        tag: v1.0.0
      portions:
        - name: auth
          description: Authentication module
          steps: []
        - name: database
          description: Database module
          steps: []
    """

    config_file = template_path / ".pyportion.yml"
    config_file.write_text(config_str)
    (base_path / ".pyportion.yml").touch()


def create_template_without_source(mock_user_data_dir: PosixPath,
                                   template_name: str) -> None:
    """Helper function to create a template without source."""
    tm = TemplateManager()
    tm.create_pyportion_dir()

    template_path = mock_user_data_dir / "pyportion" / template_name
    template_path.mkdir(parents=True)
    base_path = template_path / "base"
    base_path.mkdir()

    config_str = """\
      name: Test Template No Source
      version: 1.0.0
      description: A test template without source
      author: Test Author
      type: test
      """
    config_file = template_path / ".pyportion.yml"
    config_file.write_text(config_str)
    (base_path / ".pyportion.yml").touch()

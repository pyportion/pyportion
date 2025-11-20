import re
from pathlib import Path

from portion.base import CommandBase
from portion.core import ProjectManager
from portion.core import TemplateManager
from portion.models import ProjectTemplate
from portion.models import TemplateAskStep
from portion.models import TemplateCopyStep
from portion.models import TemplatePortion
from portion.models import TemplateReplaceStep


class BuildCommand(CommandBase):
    def __init__(self) -> None:
        super().__init__()
        self.project_manager = ProjectManager()
        self.template_manager = TemplateManager()
        self._memory: dict[str, str] = {}

    def _run_ask_step(self,
                      template: ProjectTemplate,
                      step: TemplateAskStep) -> None:
        self.logger.info(step.question)
        self._memory[step.variable] = input()

    def _resolve_variable(self, text: str) -> str:
        def repl(match: re.Match) -> str:
            key = match.group(1)
            return self._memory.get(key, match.group(0))
        return re.sub(r"\$(\w+)", repl, text)

    def _resolve_path(self, path: list[str]) -> list[str]:
        fixed_path: list[str] = []
        for part in path:
            fixed_path.append(self._resolve_variable(part))
        return fixed_path

    def _run_copy_step(self,
                       template: ProjectTemplate,
                       step: TemplateCopyStep) -> None:
        to_path = self._resolve_path(step.to_path)
        self.template_manager.copy_portion(template.name,
                                           step.from_path,
                                           to_path)

    def _run_replace_step(self,
                          template: ProjectTemplate,
                          step: TemplateReplaceStep) -> None:
        def camelcase(text: str) -> str:
            words = text.split()
            return words[0].lower() + ''.join(
                word.capitalize() for word in words[1:])

        def pascalcase(text: str) -> str:
            return ''.join(word.capitalize() for word in text.split())

        def snakecase(text: str) -> str:
            return '_'.join(text.lower().split())

        def kebabcase(text: str) -> str:
            return '-'.join(text.lower().split())

        def titlecase(text: str) -> str:
            return text.title()

        def lowercase(text: str) -> str:
            return text.lower()

        def uppercase(text: str) -> str:
            return text.upper()

        modes = {
            "camelcase": camelcase,
            "pascalcase": pascalcase,
            "snakecase": snakecase,
            "kebabcase": kebabcase,
            "titlecase": titlecase,
            "lowercase": lowercase,
            "uppercase": uppercase,
        }

        path = self._resolve_path(step.path)
        replacements: dict[str, str] = {}

        for replace in step.replacements:
            memory_value = self._resolve_variable(replace.value)
            value = modes[replace.mode](memory_value)
            replacements[replace.keyword] = value

        self.project_manager.replace_in_file(path, replacements)

    def _find_portion(self,
                      portions: list[tuple[ProjectTemplate, TemplatePortion]],
                      portion_name: str,
                      ) -> tuple[ProjectTemplate, TemplatePortion] | None:
        for template, portion in portions:
            if portion.name == portion_name:
                return template, portion
        return None

    def build(self, portion_name: str) -> None:
        path = Path.cwd()

        pconfig = self.project_manager.read_configuration(path)

        portions = [(t, portion)
                    for t in pconfig.templates
                    for portion in
                    self.template_manager.read_configuration(t.name).portions]

        template_portion = self._find_portion(portions, portion_name)

        if not template_portion:
            self.logger.error(f"There is no portion called {portion_name}")
            return None

        template, portion = template_portion

        for step in portion.steps:
            function = f"_run_{step.type.value}_step"
            getattr(self, function)(template, step)

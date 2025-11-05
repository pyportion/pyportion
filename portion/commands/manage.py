from portion.base import CommandBase


class ManageCommand(CommandBase):
    def __init__(self) -> None:
        super().__init__()

    def add(self, template_name: str) -> None:
        ...

    def remove(self, template_name: str) -> None:
        ...

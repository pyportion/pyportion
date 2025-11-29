from dataclasses import dataclass


class Message:
    @dataclass
    class Init:
        CHECKING_INIT = "Checking current path: {path}"
        PROJECT_EXIST = "This project is already a portion project"
        INITIALIZED = ("[bold cyan]{project_name}[/] project has "
                       "been initialized successfully")

from pydantic import BaseModel


class ProjectTemplate(BaseModel):
    name: str
    link: str
    tag: str


class PortionConfig(BaseModel):
    name: str
    templates: list[ProjectTemplate]

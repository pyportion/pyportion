from pydantic import BaseModel


class Template(BaseModel):
    name: str
    link: str
    tag: str


class PortionMetadata(BaseModel):
    name: str
    templates: list[Template]

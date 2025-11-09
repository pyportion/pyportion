from typing import Optional

from pydantic import BaseModel


class TemplateSource(BaseModel):
    link: str
    tag: str


class TemplateConfig(BaseModel):
    name: str
    version: str
    description: str
    author: str
    type: str

    source: Optional[TemplateSource] = None

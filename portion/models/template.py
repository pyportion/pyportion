from enum import Enum
from typing import Literal
from typing import Optional
from typing import Union

from pydantic import BaseModel


class OperationTypes(Enum):
    ASK = "ask"
    COPY = "copy"
    REPLACE = "replace"


class AskStep(BaseModel):
    type: Literal[OperationTypes.ASK]
    question: str
    variable: str


class CopyStep(BaseModel):
    type: Literal[OperationTypes.COPY]
    from_path: str
    to_path: str


class ReplaceStep(BaseModel):
    type: Literal[OperationTypes.REPLACE]
    path: str
    keyword: str
    value: str


TemplatePortionSteps = Union[AskStep, CopyStep, ReplaceStep]


class TemplatePortion(BaseModel):
    name: str
    steps: list[TemplatePortionSteps]


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
    portions: list[TemplatePortion] = []

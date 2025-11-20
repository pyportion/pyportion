from enum import Enum
from typing import Optional
from typing import Union

from pydantic import BaseModel


class OperationTypes(Enum):
    ASK = "ask"
    COPY = "copy"
    REPLACE = "replace"


class TemplateAskStep(BaseModel):
    type: OperationTypes
    question: str
    variable: str


class TemplateCopyStep(BaseModel):
    type: OperationTypes
    from_path: list[str]
    to_path: list[str]


class TemplateReplacements(BaseModel):
    keyword: str
    value: str
    mode: str


class TemplateReplaceStep(BaseModel):
    type: OperationTypes
    path: list[str]
    replacements: list[TemplateReplacements]


TemplatePortionStepsType = Union[TemplateAskStep,
                                 TemplateCopyStep,
                                 TemplateReplaceStep]


class TemplatePortion(BaseModel):
    name: str
    steps: list[TemplatePortionStepsType]


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

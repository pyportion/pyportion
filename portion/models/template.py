from enum import Enum
from typing import Literal
from typing import Optional
from typing import Union

from pydantic import BaseModel


class OperationTypes(Enum):
    ASK = "ask"
    COPY = "copy"
    REPLACE = "replace"


class TemplateAskStep(BaseModel):
    type: Literal[OperationTypes.ASK]
    question: str
    variable: str


class TemplateCopyStep(BaseModel):
    type: Literal[OperationTypes.COPY]
    from_path: str
    to_path: str


class TemplateReplaceStep(BaseModel):
    type: Literal[OperationTypes.REPLACE]
    path: str
    keyword: str
    value: str


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

from dataclasses import asdict
from dataclasses import dataclass


@dataclass
class DictMixin:
    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class Portion(DictMixin):
    name: str
    link: str
    tag: str


@dataclass
class PortionMetadata(DictMixin):
    name: str
    portions: list[Portion]

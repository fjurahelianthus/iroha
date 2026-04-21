from dataclasses import dataclass
from typing import Optional, Union

@dataclass
class IntLiteral:
    value: int

@dataclass
class FloatLiteral:
    value: float

@dataclass
class StringLiteral:
    value: str

@dataclass
class BoolLiteral:
    value: bool

Literal = Union[IntLiteral, FloatLiteral, StringLiteral, BoolLiteral]

@dataclass
class Binding:
    name: str
    type_ann: str
    value: Optional[Literal] = None


from dataclasses import dataclass, field
from typing import Optional, Union, List

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

@dataclass
class FuncCall:
    func: str
    args: list[Literal | str] = field(default_factory=list)
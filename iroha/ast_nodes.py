from dataclasses import dataclass
from typing import List, Optional

@dataclass
class IntLiteral:
    value: int

@dataclass
class Binding:
    name: str
    type_ann: str


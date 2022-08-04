from dataclasses import dataclass
from typing import Optional

from .base_dto import DTO


@dataclass
class Powerstats(DTO):
    intelligence: Optional[int] = None
    strength: Optional[int] = None
    speed: Optional[int] = None
    durability: Optional[int] = None
    power: Optional[int] = None
    combat: Optional[int] = None

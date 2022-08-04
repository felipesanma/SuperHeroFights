from dataclasses import dataclass
from typing import List, Optional

from .base_dto import DTO


@dataclass
class Appearance(DTO):
    gender: Optional[str] = None
    race: Optional[str] = None
    height: Optional[List[str]] = None
    weight: Optional[List[str]] = None
    eyeColor: Optional[str] = None
    hairColor: Optional[str] = None

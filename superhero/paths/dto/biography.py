from dataclasses import dataclass
from typing import List, Optional

from .base_dto import DTO


@dataclass
class Biography(DTO):
    fullName: Optional[str] = None
    alterEgos: Optional[str] = None
    aliases: Optional[List[str]] = None
    placeOfBirth: Optional[str] = None
    firstAppearance: Optional[str] = None
    publisher: Optional[str] = None
    alignment: Optional[str] = None

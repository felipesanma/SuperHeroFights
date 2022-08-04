from dataclasses import dataclass
from typing import Optional

from .base_dto import DTO


@dataclass
class Connections(DTO):
    groupAffiliation: Optional[str] = None
    relatives: Optional[str] = None

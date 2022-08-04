from dataclasses import dataclass
from typing import Optional

from .base_dto import DTO


@dataclass
class Work(DTO):
    occupation: Optional[str] = None
    base: Optional[str] = None

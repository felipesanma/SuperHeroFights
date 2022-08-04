from dataclasses import dataclass
from typing import Literal, Optional

from .base_dto import DTO


@dataclass
class Images(DTO):
    xs: Optional[str] = None
    sm: Optional[str] = None
    md: Optional[str] = None
    lg: Optional[str] = None


@dataclass
class ImageSize(DTO):
    size: Optional[Literal["xs", "sm", "md", "lg"]]

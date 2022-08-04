from dataclasses import dataclass
from typing import Optional

from .appearance import Appearance
from .base_dto import DTO
from .biography import Biography
from .connections import Connections
from .images import Images
from .powerstats import Powerstats
from .work import Work


@dataclass
class SuperHeroCompleteInformation(DTO):
    id: Optional[int] = None
    name: Optional[str] = None
    slug: Optional[str] = None
    powerstats: Optional[Powerstats] = None
    appearance: Optional[Appearance] = None
    biography: Optional[Biography] = None
    work: Optional[Work] = None
    connections: Optional[Connections] = None
    images: Optional[Images] = None

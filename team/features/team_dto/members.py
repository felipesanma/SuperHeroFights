from dataclasses import dataclass
from typing import Optional, Union


@dataclass
class Stats:
    intelligence: Optional[int] = None
    strength: Optional[int] = None
    speed: Optional[int] = None
    durability: Optional[int] = None
    power: Optional[int] = None
    combat: Optional[int] = None


@dataclass
class Attacks:
    mental: Optional[Union[int, float]] = None
    strong: Optional[Union[int, float]] = None
    fast: Optional[Union[int, float]] = None


@dataclass
class AvatarImages:
    xs: Optional[str] = None
    sm: Optional[str] = None
    md: Optional[str] = None
    lg: Optional[str] = None


@dataclass
class MemberInTraining:
    name: Optional[str] = None
    id: Optional[int] = None
    alignment: Optional[str] = None
    avatar: Optional[AvatarImages] = None
    fb: Optional[Union[int, float]] = None
    hp: Optional[Union[int, float]] = None
    power_stats: Optional[Stats] = None
    fight_stats: Optional[Stats] = None
    attacks: Optional[Attacks] = None
    is_aligned: Optional[bool] = None
    ready_to_fight: Optional[bool] = None

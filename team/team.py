from collections import namedtuple

from .features import TeamManagement, TeamTraining


class Team:
    """
    Generador de equipo (máximo 5 miembros)
    """

    def __init__(
        self,
        *,
        members: list = None,
        alignment: str = None,
        ready_to_fight: bool = False
    ):
        config = namedtuple("config", ["members", "alignment", "ready_to_fight"])

        cfg = config(members, alignment, ready_to_fight)

        self.manage = TeamManagement(cfg)
        self.train = TeamTraining(cfg)
        self.members = members
        self.alignment = alignment
        self.ready_to_fight = ready_to_fight

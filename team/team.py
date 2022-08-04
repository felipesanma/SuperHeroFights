from .features import TeamManagement, TeamTraining


class Team:
    """
    Generador de equipo (máximo 5 miembros)
    """

    def __init__(
        self, *, members: list = [], alignment: str = None, ready_to_fight: bool = False
    ):

        self.manage = TeamManagement(members=members)
        self.train = TeamTraining(alignment=alignment, members=members)
        self.members = self.manage.members_names
        # self.alignment = alignment
        # self.ready_to_fight = ready_to_fight

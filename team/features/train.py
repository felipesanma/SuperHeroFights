from .config import MAX_HERO_MEMBERS


class TeamTraining:
    """
    Entrenamiento del equipo
    """

    def __init__(self, *, members: list):

        if len(members) != MAX_HERO_MEMBERS:
            raise ("Not enough members. For train a team you need more members")
        self.members = members

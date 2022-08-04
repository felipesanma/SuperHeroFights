from .config import MAX_HERO_MEMBERS


class TeamTraining:
    """
    Entrenamiento del equipo
    """

    def __init__(self, *, members: list):
        print("len(members)", len(members))
        print("MAX_HERO_MEMBERS: ", MAX_HERO_MEMBERS)
        if len(members) != MAX_HERO_MEMBERS:
            raise ("Not enough members. For train a team you need more members")
        self.members = members

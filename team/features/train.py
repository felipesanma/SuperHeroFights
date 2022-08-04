from .config import MAX_HERO_MEMBERS


class TeamTraining:
    """
    Entrenamiento del equipo
    """

    def __init__(self, *, members: list):
        self.members = members

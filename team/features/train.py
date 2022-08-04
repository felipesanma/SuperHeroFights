from .config import MAX_HERO_MEMBERS


class TeamTraining:
    """
    Entrenamiento del equipo
    """

    def __init__(self, *, members: list):
        self.members = members

    def actual_stamina(self):
        """
        AS: Actual Stamina, valor aleatorio antre 0 y 10
        """
        NotImplementedError

    def hp(self):
        NotImplementedError

    def get_team_alignment(self):
        """
        Alignment: será el de la mayoría.
        """
        NotImplementedError

    def fb(self):
        """
        Filiation Coefficient: bonus o penalización, según la naturaleza del personaje vs la de su equipo
        """
        NotImplementedError

    def fight_stats(self):
        NotImplementedError

    def mental_attack(self):
        NotImplementedError

    def strong_attack(self):
        NotImplementedError

    def fast_attack(self):
        NotImplementedError

    def all_attacks(self):
        NotImplementedError

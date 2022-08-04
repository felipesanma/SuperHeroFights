from typing import List

from .superhero.paths.superhero_api_dto import SuperHeroCompleteInformation
from .team_dto import MemberInTraining


class TeamTraining:
    """
    Entrenamiento del equipo
    """

    def __init__(self, *, members: list):
        self.members = self._convert_to_train_member(members)

    def _convert_to_train_member(
        self, members: List[SuperHeroCompleteInformation]
    ) -> MemberInTraining:
        members_in_training = []
        for member in members:
            member_train = MemberInTraining(
                name=member.name,
                id=member.id,
                alignment=member.biography["alignment"],
                power_stats=member.powerstats,
                fight_stats=None,
                attacks=None,
                is_aligned=None,
                ready_to_fight=False,
            )
            members_in_training.append(member_train)
        return members_in_training

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

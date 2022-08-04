import random
from typing import List

from .superhero.paths.superhero_api_dto import SuperHeroCompleteInformation
from .team_dto import MemberInTraining


class TeamTraining:
    """
    Entrenamiento del equipo
    """

    def __init__(self, *, members: list):
        self.members = self._convert_to_train_member(members)
        self.team_alignment = self.get_team_alignment()

    def _convert_to_train_member(
        self, members: List[SuperHeroCompleteInformation]
    ) -> MemberInTraining:
        members_in_training = []
        for member in members:
            member_train = MemberInTraining(
                name=member.name,
                id=member.id,
                alignment=member.biography["alignment"],
                avatar=member.images["xs"],
                power_stats=member.powerstats,
            )
            members_in_training.append(member_train)
        return members_in_training

    def actual_stamina(self) -> int:
        """
        AS: Actual Stamina, valor aleatorio antre 0 y 10
        """
        return random.randint(0, 10)

    def hp(self):
        NotImplementedError

    def get_team_alignment(self) -> str:
        """
        Alignment: será el de la mayoría.
        """
        result = ""
        team_alignment = {}
        for member in self.members:
            if member.alignment in team_alignment:
                team_alignment[member.alignment] += 1
                if team_alignment[member.alignment] > 2:
                    result = member.alignment
                    break
            else:
                team_alignment[member.alignment] = 1
        print("team_alignment_count: ", team_alignment)
        return result

    def fb(self) -> None:
        """
        Filiation Coefficient: bonus o penalización, según la naturaleza del personaje vs la de su equipo
        """
        fb = None
        for member in self.members:

            if member.alignment == self.team_alignment:
                fb = 1 + random.randint(0, 9)
                member.is_aligned = True
            else:
                fb = round(1 / (1 + random.randint(0, 9)), 2)
                member.is_aligned = False

            member.fb = fb
            print(member.name, member.fb, member.is_aligned, member.alignment)

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

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
                avatar=member.images,
                power_stats=member.powerstats,
            )
            members_in_training.append(member_train)
        return members_in_training

    def actual_stamina(self):
        """
        AS: Actual Stamina, valor aleatorio antre 0 y 10
        """
        return random.randint(0, 10)

    def hp(self) -> None:
        """
        Health Points o puntos de vida.
        """

        def stats_contribution(member):

            str_con = 0.8 * member.fight_stats["strength"]
            dbt_con = 0.7 * member.fight_stats["durability"]
            pw_con = member.fight_stats["power"]
            return (str_con + dbt_con + pw_con) / 2

        for member in self.members:

            member.hp = int(
                round(
                    100
                    + (1 + (self.actual_stamina() / 10)) * (stats_contribution(member)),
                    0,
                )
            )

        print("Health Points ready")

    def hp_increment_by_factor(self, factor: int) -> None:

        for member in self.members:
            member.hp = member.hp * factor

        print(f"Health Points incremented by {factor}")

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
        print(f"Team Alignment is '{result}'")
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
        print("Filiation Coefficient ready")

    def fight_stats(self) -> None:
        def fs(v, fb) -> float | int:
            return int(round((fb / 1.1) * (2 * v + self.actual_stamina()), 0))

        for member in self.members:

            member.fight_stats = {
                k: fs(v, member.fb) for k, v in member.power_stats.items()
            }

        print("Fight Stats ready")

    def mental_attack(self, member):
        int_con = 0.7 * member.fight_stats["intelligence"]
        spd_con = 0.2 * member.fight_stats["speed"]
        cbt_con = 0.1 * member.fight_stats["combat"]
        stats_con = int_con + spd_con + cbt_con
        return round(member.fb * (stats_con), 1)

    def strong_attack(self, member):
        str_con = 0.6 * member.fight_stats["strength"]
        pw_con = 0.2 * member.fight_stats["power"]
        cbt_con = 0.2 * member.fight_stats["combat"]
        stats_con = str_con + pw_con + cbt_con
        return round(member.fb * (stats_con), 1)

    def fast_attack(self, member):
        str_con = 0.2 * member.fight_stats["strength"]
        spd_con = 0.55 * member.fight_stats["speed"]
        dbt_con = 0.25 * member.fight_stats["durability"]
        stats_con = str_con + spd_con + dbt_con
        return round(member.fb * (stats_con), 1)

    def all_attacks(self) -> None:

        for member in self.members:

            member.attacks = {
                "mental": self.mental_attack(member),
                "strong": self.strong_attack(member),
                "fast": self.fast_attack(member),
            }

        print("Attacks ready")

    def ready_to_fight(self) -> None:

        for member in self.members:

            member.ready_to_fight = True

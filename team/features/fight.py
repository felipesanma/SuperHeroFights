import random
from typing import List

from .team_dto import MemberInFight, MemberInTraining


class TeamFight:
    """
    Pelea del equipo
    """

    def __init__(self, *, members: list):
        self.members = self._convert_to_fight_member(members)

    def _convert_to_fight_member(
        self, members: List[MemberInTraining]
    ) -> MemberInFight:
        members_in_fight = []
        for member in members:
            member_fight = MemberInFight(
                name=member.name,
                id=member.id,
                avatar=member.avatar,
                hp=member.hp,
                attacks=member.attacks,
                is_alive=True,
            )
            members_in_fight.append(member_fight)
        return members_in_fight

    def choose_random_alive_member(self) -> MemberInFight:
        alive_members = [member for member in self.members if member.is_alive]
        member_going_to_fight = random.choice(alive_members)
        print(f"Member going to fight: {member_going_to_fight.name}")
        return member_going_to_fight

    def mental_attack(self, member: MemberInFight) -> float | int:
        return member.attacks["mental"]

    def strong_attack(self, member: MemberInFight) -> float | int:
        return member.attacks["strong"]

    def fast_attack(self, member: MemberInFight) -> float | int:
        return member.attacks["fast"]

    def random_attack(self, member: MemberInFight):
        NotImplementedError

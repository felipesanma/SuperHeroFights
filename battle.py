import random

from team import Team
from team.features.config import POSSIBLE_HEROE_ID


class Battle:
    """
    Generador de batllas entre 2 equipos
    """

    def __init__(
        self, *, name_team_1: str = "Team 1", name_team_2: str = "Team 2"
    ) -> None:

        self._team_1 = Team(name=name_team_1)
        self._team_2 = Team(name=name_team_2)

    def create_teams(self) -> None:

        unique_ids = self._get_unique_heroes_ids()
        ids_team_1 = unique_ids[:5]
        ids_team_2 = unique_ids[5:10]
        print(f"Creating Team 1 '{self._team_1.name}'")
        self._team_1.manage.add_multiple_by_id(ids_team_1)
        print(f"Creating Team 2 '{self._team_2.name}'")
        self._team_2.manage.add_multiple_by_id(ids_team_2)
        self._team_1.create()
        self._team_2.create()
        print(f"{self._team_1.name}: {self._team_1.members_names}")
        print(f"{self._team_2.name}: {self._team_2.members_names}")
        print(f"Team 1 '{self._team_1.name}' and Team 2 '{self._team_2.name}' created")

    def _get_unique_heroes_ids(self) -> list:
        unique_ids = []
        for i in range(10):
            id = random.choice(tuple(POSSIBLE_HEROE_ID))
            while id in unique_ids:
                msg = f"Heroe id={id}, already exist in team. Trying with another id"
                print(msg)
                id = random.choice(tuple(POSSIBLE_HEROE_ID))
            unique_ids.append(id)
        return unique_ids

    def prepare_teams_to_fight(self) -> None:
        self._team_1.prepare_to_fight()
        self._team_2.prepare_to_fight()
        print(
            f"Team 1 '{self._team_1.name}' and Team 2 '{self._team_2.name}' are ready to fight"
        )

from .features import MAX_HERO_MEMBERS, TeamFight, TeamManagement, TeamTraining


class Team:
    """
    Generador de equipo (máximo {MAX_HERO_MEMBERS} miembros)
    """

    def __init__(
        self, *, name: str = "", members: list = [], ready_to_fight: bool = False
    ):
        self.name = name
        self.manage = TeamManagement(members=members)
        self.members_names = self.manage.members_names
        self.members = self.manage.members
        self.members_by_id = self.manage.members_id
        self.ready_to_fight = ready_to_fight

    def _set_train(self):
        if len(self.manage.members) != MAX_HERO_MEMBERS:
            n_of_heroes = MAX_HERO_MEMBERS - len(self.manage.members)
            self.manage.add_multiple_random(n_of_heroes)
        self.train = TeamTraining(members=self.manage.members)
        self.members_training = self.train.members
        self.alignment = self.train.team_alignment
        print(f"Team '{self.name}' is ready to train")

    def create(self):
        print(f"Preparing Team '{self.name}'")
        self._set_train()

    def prepare_to_fight(self):
        print(f"Preparing team '{self.name}' to fight")
        self.train.fb()
        self.train.fight_stats()
        self.train.all_attacks()
        self.train.hp()
        self.train.ready_to_fight()
        self.fight = TeamFight(members=self.members_training)
        self.members_fighting = self.fight.members
        print(f"Team '{self.name}' is ready to fight")

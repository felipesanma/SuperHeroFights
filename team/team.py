from .features import MAX_HERO_MEMBERS, TeamManagement, TeamTraining


class Team:
    """
    Generador de equipo (máximo 5 miembros)
    """

    def __init__(self, *, members: list = [], ready_to_fight: bool = False):

        self.manage = TeamManagement(members=members)
        self.members_names = self.manage.members_names
        self.members = self.manage.members
        self.members_by_id = self.manage.members_id
        self.ready_to_fight = ready_to_fight
        # self.alignment = alignment
        # self.ready_to_fight = ready_to_fight

    def set_train(self):
        if len(self.manage.members) != MAX_HERO_MEMBERS:
            n_of_heroes = MAX_HERO_MEMBERS - len(self.manage.members)
            self.manage.add_multiple_random(n_of_heroes)
        self.train = TeamTraining(members=self.manage.members)
        print("Team ready to train")
        print(self.manage.members_id)

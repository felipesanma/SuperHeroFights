import random

from .superhero import SuperHero

# Reference: https://akabab.github.io/superhero-api/api/glossary.html
FIRST_HERO_ID = 1
LAST_HERO_ID = 731
# Declared on task
MAX_HERO_MEMBERS = 5


class TeamManagement:
    """
    Administración del equipo
    """

    def __init__(self, *, members: list):
        self.members = members
        self.members_names = []
        self.members_id = {}

    def add_member_by_id(self, id: int):

        if len(self.members_names) == MAX_HERO_MEMBERS:
            msg = f"Team already has 5 members, try removing members first"
            print(msg)
            return msg, 405

        superhero = SuperHero(id=id)
        superheroe, status_code = superhero.characters.get_complete_information()

        if status_code != 200:
            msg = f"No heroe found for id={id}, try with another id"
            print(msg)
            return msg, status_code

        if superheroe.id in self.members_id:
            msg = f"Heroe id={id}, already exist in team. Try with another id"
            print(msg)
            return msg, 406

        self.members.append(superheroe)
        self.members_names.append(superheroe.name)
        self.members_id[superheroe.id] = superheroe.name

        msg = f"NEW HEROE ADDED: {superheroe.name}"
        print(msg)
        return msg, 200

    def add_random_member(self):

        if len(self.members_names) == MAX_HERO_MEMBERS:
            msg = f"Team already has 5 members, try removing members first"
            print(msg)
            return msg, 405

        id = random.randint(FIRST_HERO_ID, LAST_HERO_ID)

        superhero = SuperHero(id=id)
        superheroe, status_code = superhero.characters.get_complete_information()

        if status_code != 200:
            msg = f"No heroe found for id={id}, try with another id"
            print(msg)
            return msg, status_code

        if superheroe.id in self.members_id:
            msg = f"Heroe id={id}, already exist in team. Try with another id"
            print(msg)
            return msg, 404

        self.members.append(superheroe)
        self.members_names.append(superheroe.name)
        self.members_id[superheroe.id] = superheroe.name

        msg = f"NEW HEROE ADDED: {superheroe.name}"
        print(msg)
        return msg, 200

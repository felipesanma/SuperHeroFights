import random

from .config import MAX_HERO_MEMBERS, POSSIBLE_HEROE_ID
from .superhero import SuperHero


class TeamManagement:
    """
    Administración del equipo
    """

    def __init__(self, *, members: list):
        self.members = members
        self.members_names = []
        self.members_id = {}

    def add_member_by_id(self, id: int):

        if id not in POSSIBLE_HEROE_ID:
            msg = f"No heroe found for id={id}, try with another id"
            print(msg)
            return msg, 404

        if len(self.members_names) == MAX_HERO_MEMBERS:
            msg = f"Team already has 5 members, try removing members first"
            print(msg)
            return msg, 405

        if id in self.members_id:
            msg = f"Heroe id={id}, already exist in team. Try with another id"
            print(msg)
            return msg, 406

        superhero = SuperHero(id=id)
        superheroe, status_code = superhero.characters.get_complete_information()

        self.members.append(superheroe)
        self.members_names.append(superheroe.name)
        self.members_id[id] = superheroe.name

        msg = f"NEW HEROE ADDED: {superheroe.name}"
        print(msg)
        return msg, status_code

    def add_random_member(self):

        if len(self.members_names) == MAX_HERO_MEMBERS:
            msg = f"Team already has 5 members, try removing members first"
            print(msg)
            return msg, 405

        id = random.choice(tuple(POSSIBLE_HEROE_ID))

        if id in self.members_id:
            msg = f"Heroe id={id}, already exist in team. Try with another id"
            print(msg)
            return msg, 406

        superhero = SuperHero(id=id)
        superheroe, status_code = superhero.characters.get_complete_information()

        self.members.append(superheroe)
        self.members_names.append(superheroe.name)
        self.members_id[id] = superheroe.name

        msg = f"NEW HEROE ADDED: {superheroe.name}"
        print(msg)
        return msg, status_code

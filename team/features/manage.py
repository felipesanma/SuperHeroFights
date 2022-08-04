import random

from .config import MAX_HERO_MEMBERS, POSSIBLE_HEROE_ID
from .superhero import SuperHero


class TeamManagement:
    """
    Administración del equipo
    """

    def __init__(self, *, members: list) -> None:
        self.members = members
        self.members_names = []
        self.members_id = {}

    def add_member_by_id(self, id: int):

        if id not in POSSIBLE_HEROE_ID:
            msg = f"Sorry! No heroe found for id={id}, try with another id"
            print(msg)
            return msg, 404

        if len(self.members_names) == MAX_HERO_MEMBERS:
            msg = f"Team already has {MAX_HERO_MEMBERS} members, try removing members first. Hero id: {id}"
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
            msg = f"Team already has {MAX_HERO_MEMBERS} members, try removing members first. Hero id: {id}"
            print(msg)
            return msg, 405

        id = random.choice(tuple(POSSIBLE_HEROE_ID))

        while id in self.members_id:
            msg = f"Heroe id={id}, already exist in team. Trying with another id"
            print(msg)
            id = random.choice(tuple(POSSIBLE_HEROE_ID))

        superhero = SuperHero(id=id)
        superheroe, status_code = superhero.characters.get_complete_information()

        self.members.append(superheroe)
        self.members_names.append(superheroe.name)
        self.members_id[id] = superheroe.name

        msg = f"NEW HEROE ADDED: {superheroe.name}"
        print(msg)
        return msg, status_code

    def add_multiple_by_id(self, ids: list) -> None:
        for id in ids:
            self.add_member_by_id(id)

    def add_multiple_random(self, quantity: int) -> None:
        for i in range(quantity):
            self.add_random_member()

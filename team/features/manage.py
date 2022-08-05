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

        msg = f"New member: {superheroe.name}"
        print(msg)
        return msg, status_code

    def add_random_member(self):

        id = random.choice(tuple(POSSIBLE_HEROE_ID))

        if len(self.members_names) == MAX_HERO_MEMBERS:
            msg = f"Team already has {MAX_HERO_MEMBERS} members, try removing members first. Hero id: {id}"
            print(msg)
            return msg, 405

        while id in self.members_id:
            msg = f"Heroe id={id}, already exist in team. Trying with another id"
            print(msg)
            id = random.choice(tuple(POSSIBLE_HEROE_ID))

        superhero = SuperHero(id=id)
        superheroe, status_code = superhero.characters.get_complete_information()

        self.members.append(superheroe)
        self.members_names.append(superheroe.name)
        self.members_id[id] = superheroe.name

        msg = f"New member: {superheroe.name}"
        print(msg)
        return msg, status_code

    def add_multiple_by_id(self, ids: list) -> None:
        for id in ids:
            self.add_member_by_id(id)

    def add_multiple_random(self, quantity: int) -> None:
        for i in range(quantity):
            self.add_random_member()

    def remove_member_by_id(self, id: int) -> None:

        if id not in self.members_id:
            msg = f"Heroe id={id}, not exist in team. Check members id in members_id object"
            print(msg)
            return msg, 407

        removed_member_from_id = self.members_id.pop(id)
        for i, hero_name in enumerate(self.members_names):
            if hero_name == removed_member_from_id:
                removed_member_from_name = self.members_names.pop(i)
                removed_member_from_members = self.members.pop(i)

        print(f"Removed: Heroe {removed_member_from_id} id: {id}")

    def remove_all_members(self) -> None:
        self.members.clear()
        self.members_names.clear()
        self.members_id.clear()
        print("All members removed")

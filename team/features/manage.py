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

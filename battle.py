import random
import time

import streamlit as st

from team import Team
from team.features.config import POSSIBLE_HEROE_ID
from team.features.team_dto.members import MemberInFight


class Battle:
    """
    Generador de batallas entre 2 equipos
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
        print(f"Creating '{self._team_1.name}'")
        self._team_1.manage.add_multiple_by_id(ids_team_1)
        print(f"Creating '{self._team_2.name}'")
        self._team_2.manage.add_multiple_by_id(ids_team_2)
        self._team_1.create()
        self._team_2.create()
        print(f"{self._team_1.name}: {self._team_1.members_names}")
        print(f"{self._team_2.name}: {self._team_2.members_names}")
        print(f"'{self._team_1.name}' and '{self._team_2.name}' created")

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
        print(f"'{self._team_1.name}' and '{self._team_2.name}' are ready to fight")

    def _start_heroes_fight(self, hero_1: MemberInFight, hero_2: MemberInFight):
        hp_1 = hero_1.hp
        hp_2 = hero_2.hp
        winner = None
        looser = None
        while hp_1 > 0 and hp_2 > 0:

            attack_name_hero_1, attack_damage_hero_1 = self._team_1.fight.random_attack(
                hero_1
            )

            attack_name_hero_2, attack_damage_hero_2 = self._team_2.fight.random_attack(
                hero_2
            )

            print(
                f"{hero_1.name} attacks with {attack_name_hero_1} dealing {attack_damage_hero_1}"
            )
            time.sleep(1)
            hp_2 -= attack_damage_hero_1
            if hp_2 < 0:
                print(f"{hero_2.name} now has 0 HP")
                winner = hero_1
                looser = hero_2
                break
            print(f"{hero_2.name} now has {hp_2} HP")
            time.sleep(1)
            print(
                f"{hero_2.name} attack with {attack_name_hero_2} dealing {attack_damage_hero_2}"
            )
            time.sleep(1)
            hp_1 -= attack_damage_hero_2
            if hp_1 < 0:
                print(f"{hero_1.name} now has 0 HP")
                winner = hero_2
                looser = hero_1
                break
            print(f"{hero_1.name} now has {hp_1} HP")
        time.sleep(1)
        return winner, looser

    def _choose_alive_heroes_to_fight(self):

        hero_team_1 = self._team_1.fight.choose_random_alive_member()
        hero_team_2 = self._team_2.fight.choose_random_alive_member()

        return hero_team_1, hero_team_2

    def _get_alive_heroes_in_battle(self):

        alive_heroes_team_1 = [
            member for member in self._team_1.members_fighting if member.is_alive
        ]
        alive_heroes_team_2 = [
            member for member in self._team_2.members_fighting if member.is_alive
        ]
        time.sleep(1)
        print(f"Alive members for '{self._team_1.name}': {len(alive_heroes_team_1)}")
        time.sleep(1)
        print(f"Alive members for '{self._team_2.name}': {len(alive_heroes_team_2)}")

        return len(alive_heroes_team_1), len(alive_heroes_team_2)

    def start(self) -> None:
        print("Battle Starts Now!!")
        alive_heroes_team_1, alive_heroes_team_2 = self._get_alive_heroes_in_battle()
        fights = 0
        winner = None
        while alive_heroes_team_1 > 0 and alive_heroes_team_2 > 0:
            if fights == 0:
                hero_team_1, hero_team_2 = self._choose_alive_heroes_to_fight()
            else:

                if winner.id in self._team_1.members_by_id:
                    hero_team_1 = winner
                    hero_team_2 = self._team_2.fight.choose_random_alive_member()
                else:
                    hero_team_2 = winner
                    hero_team_1 = self._team_1.fight.choose_random_alive_member()

            time.sleep(1)
            print(f"'{self._team_1.name}' choose hero: {hero_team_1.name}")
            time.sleep(1)
            print(f"'{self._team_2.name}' choose hero: {hero_team_2.name}")
            time.sleep(1)
            winner, looser = self._start_heroes_fight(hero_team_1, hero_team_2)
            print(f"{winner.name} won!")
            time.sleep(1)
            if winner.id in self._team_1.members_by_id:
                for member in self._team_2.members_fighting:
                    if member.id == looser.id:
                        member.is_alive = False
            else:
                for member in self._team_1.members_fighting:
                    if member.id == looser.id:
                        member.is_alive = False

            (
                alive_heroes_team_1,
                alive_heroes_team_2,
            ) = self._get_alive_heroes_in_battle()
            fights += 1
        battle_winner = None
        if alive_heroes_team_1 > 0:
            battle_winner = self._team_1
        else:
            battle_winner = self._team_2
        time.sleep(1)
        print(f"Winner Team Battle '{battle_winner.name}'")

    def _streamlit_heroes_fight(
        self, hero_1: MemberInFight, hero_2: MemberInFight, message
    ):
        hp_1 = hero_1.hp
        hp_2 = hero_2.hp
        winner = None
        looser = None
        fight_messages = []
        while hp_1 > 0 and hp_2 > 0:

            attack_name_hero_1, attack_damage_hero_1 = self._team_1.fight.random_attack(
                hero_1
            )

            attack_name_hero_2, attack_damage_hero_2 = self._team_2.fight.random_attack(
                hero_2
            )
            text = f"{hero_1.name} attacks with {attack_name_hero_1} dealing {attack_damage_hero_1} damage"
            fight_messages.append(text)
            for i in range(len(text) + 1):
                message.markdown("## %s" % text[0:i])
                time.sleep(0.05)
            time.sleep(1)
            hp_2 -= attack_damage_hero_1
            if hp_2 < 0:
                text = f"{hero_2.name} has no HP"
                fight_messages.append(text)
                for i in range(len(text) + 1):
                    message.markdown("## %s" % text[0:i])
                    time.sleep(0.05)
                winner = hero_1
                looser = hero_2
                break
            text = f"{hero_2.name} now has {int(hp_2)} HP"
            fight_messages.append(text)
            for i in range(len(text) + 1):
                message.markdown("## %s" % text[0:i])
                time.sleep(0.05)
            time.sleep(1)

            text = f"{hero_2.name} attack with {attack_name_hero_2} dealing {attack_damage_hero_2} damage"
            fight_messages.append(text)
            for i in range(len(text) + 1):
                message.markdown("## %s" % text[0:i])
                time.sleep(0.05)
            time.sleep(1)
            hp_1 -= attack_damage_hero_2
            if hp_1 < 0:
                text = f"{hero_1.name} has no HP"
                fight_messages.append(text)
                for i in range(len(text) + 1):
                    message.markdown("## %s" % text[0:i])
                    time.sleep(0.05)
                winner = hero_2
                looser = hero_1
                break
            text = f"{hero_1.name} now has {int(hp_1)} HP"
            fight_messages.append(text)
            for i in range(len(text) + 1):
                message.markdown("## %s" % text[0:i])
                time.sleep(0.05)
            time.sleep(1)
        time.sleep(1)
        return winner, looser, fight_messages

    def streamlit_start(self) -> None:
        message = st.empty()
        text = "Battle Starts Now!!"
        for i in range(len(text) + 1):
            message.markdown("## %s" % text[0:i])
            time.sleep(0.05)
        alive_heroes_team_1, alive_heroes_team_2 = self._get_alive_heroes_in_battle()
        fights = 0
        winner = None
        battle_history = []
        while alive_heroes_team_1 > 0 and alive_heroes_team_2 > 0:
            if fights == 0:
                hero_team_1, hero_team_2 = self._choose_alive_heroes_to_fight()
            else:

                if winner.id in self._team_1.members_by_id:
                    hero_team_1 = winner
                    hero_team_2 = self._team_2.fight.choose_random_alive_member()
                else:
                    hero_team_2 = winner
                    hero_team_1 = self._team_1.fight.choose_random_alive_member()
            text = f"Fight N??: {fights+1}"
            for i in range(len(text) + 1):
                message.markdown("## %s" % text[0:i])
                time.sleep(0.05)
            time.sleep(1)
            text = f"{self._team_1.name} choose: {hero_team_1.name}"
            for i in range(len(text) + 1):
                message.markdown("## %s" % text[0:i])
                time.sleep(0.05)
            time.sleep(1)
            text = f"{self._team_2.name} choose: {hero_team_2.name}"
            for i in range(len(text) + 1):
                message.markdown("## %s" % text[0:i])
                time.sleep(0.05)
            time.sleep(1)
            text = f"Ready.....?"
            for i in range(len(text) + 1):
                message.markdown("## %s" % text[0:i])
                time.sleep(0.05)
            time.sleep(0.5)
            text = f"Go!"
            for i in range(len(text) + 1):
                message.markdown("## %s" % text[0:i])
                time.sleep(0.05)
            time.sleep(0.5)
            winner, looser, fight_messages = self._streamlit_heroes_fight(
                hero_team_1, hero_team_2, message
            )
            text = f"{winner.name} won!"
            for i in range(len(text) + 1):
                message.markdown("## %s" % text[0:i])
                time.sleep(0.05)
            st.balloons()
            time.sleep(1)
            if winner.id in self._team_1.members_by_id:
                for member in self._team_2.members_fighting:
                    if member.id == looser.id:
                        member.is_alive = False
            else:
                for member in self._team_1.members_fighting:
                    if member.id == looser.id:
                        member.is_alive = False

            (
                alive_heroes_team_1,
                alive_heroes_team_2,
            ) = self._get_alive_heroes_in_battle()

            event_fight = {
                "fight": fights + 1,
                "messages": fight_messages,
                "winner": winner,
                "looser": looser,
            }
            battle_history.append(event_fight)
            fights += 1
        battle_winner = None
        if alive_heroes_team_1 > 0:
            battle_winner = self._team_1
            battle_looser = self._team_2

            alive_heroes_winner = alive_heroes_team_1
        else:
            battle_winner = self._team_2
            battle_looser = self._team_1

            alive_heroes_winner = alive_heroes_team_2
        time.sleep(1)
        text = f"Winner Team Battle '{battle_winner.name}'"
        for i in range(len(text) + 1):
            message.markdown("## %s" % text[0:i])
            time.sleep(0.05)
        st.snow()
        battle_info = {
            "winner": {
                "team_name": battle_winner.name,
                "alive_heroes": alive_heroes_winner,
                "death_heroes": 5 - alive_heroes_winner,
                "alignment": battle_winner.alignment,
                "heroes": {
                    "original_info": battle_winner.members,
                    "after_training": battle_winner.members_training,
                    "ready_to_fighting": battle_winner.members_fighting,
                },
            },
            "looser": {
                "team_name": battle_looser.name,
                "alive_heroes": 0,
                "death_heroes": 5,
                "alignment": battle_looser.alignment,
                "heroes": {
                    "original_info": battle_looser.members,
                    "after_training": battle_looser.members_training,
                    "ready_to_fighting": battle_looser.members_fighting,
                },
            },
            "total_fights": fights,
        }
        return battle_info, battle_history

    def _streamlit_heroes_quick_fight(
        self, hero_1: MemberInFight, hero_2: MemberInFight
    ):
        hp_1 = hero_1.hp
        hp_2 = hero_2.hp
        winner = None
        looser = None
        fight_messages = []
        while hp_1 > 0 and hp_2 > 0:

            attack_name_hero_1, attack_damage_hero_1 = self._team_1.fight.random_attack(
                hero_1
            )

            attack_name_hero_2, attack_damage_hero_2 = self._team_2.fight.random_attack(
                hero_2
            )
            text = f"{hero_1.name} attacks with {attack_name_hero_1} dealing {attack_damage_hero_1} damage"
            fight_messages.append(text)
            hp_2 -= attack_damage_hero_1
            if hp_2 < 0:
                text = f"{hero_2.name} has no HP"
                fight_messages.append(text)
                winner = hero_1
                looser = hero_2
                break
            text = f"{hero_2.name} now has {int(hp_2)} HP"
            fight_messages.append(text)
            text = f"{hero_2.name} attack with {attack_name_hero_2} dealing {attack_damage_hero_2} damage"
            fight_messages.append(text)
            hp_1 -= attack_damage_hero_2
            if hp_1 < 0:
                text = f"{hero_1.name} has no HP"
                fight_messages.append(text)
                winner = hero_2
                looser = hero_1
                break
            text = f"{hero_1.name} now has {int(hp_1)} HP"
            fight_messages.append(text)
        return winner, looser, fight_messages

    def streamlit_fast_battle_start(self) -> None:
        alive_heroes_team_1, alive_heroes_team_2 = self._get_alive_heroes_in_battle()
        fights = 0
        winner = None
        battle_history = []
        while alive_heroes_team_1 > 0 and alive_heroes_team_2 > 0:
            if fights == 0:
                hero_team_1, hero_team_2 = self._choose_alive_heroes_to_fight()
            else:

                if winner.id in self._team_1.members_by_id:
                    hero_team_1 = winner
                    hero_team_2 = self._team_2.fight.choose_random_alive_member()
                else:
                    hero_team_2 = winner
                    hero_team_1 = self._team_1.fight.choose_random_alive_member()

            winner, looser, fight_messages = self._streamlit_heroes_quick_fight(
                hero_team_1, hero_team_2
            )
            if winner.id in self._team_1.members_by_id:
                for member in self._team_2.members_fighting:
                    if member.id == looser.id:
                        member.is_alive = False
            else:
                for member in self._team_1.members_fighting:
                    if member.id == looser.id:
                        member.is_alive = False

            (
                alive_heroes_team_1,
                alive_heroes_team_2,
            ) = self._get_alive_heroes_in_battle()

            event_fight = {
                "fight": fights + 1,
                "messages": fight_messages,
                "winner": winner,
                "looser": looser,
            }
            battle_history.append(event_fight)
            fights += 1
        battle_winner = None
        if alive_heroes_team_1 > 0:
            battle_winner = self._team_1
            battle_looser = self._team_2

            alive_heroes_winner = alive_heroes_team_1
        else:
            battle_winner = self._team_2
            battle_looser = self._team_1

            alive_heroes_winner = alive_heroes_team_2
        st.snow()
        battle_info = {
            "winner": {
                "team_name": battle_winner.name,
                "alive_heroes": alive_heroes_winner,
                "death_heroes": 5 - alive_heroes_winner,
                "alignment": battle_winner.alignment,
                "heroes": {
                    "original_info": battle_winner.members,
                    "after_training": battle_winner.members_training,
                    "ready_to_fighting": battle_winner.members_fighting,
                },
            },
            "looser": {
                "team_name": battle_looser.name,
                "alive_heroes": 0,
                "death_heroes": 5,
                "alignment": battle_looser.alignment,
                "heroes": {
                    "original_info": battle_looser.members,
                    "after_training": battle_looser.members_training,
                    "ready_to_fighting": battle_looser.members_fighting,
                },
            },
            "total_fights": fights,
        }
        return battle_info, battle_history

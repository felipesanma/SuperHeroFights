from ctypes import alignment

from team import Team

"""
print('INIT: TEAM 1')
# Test add_member_by_id method
team = Team()
hero_id = 1
new_member = team.manage.add_member_by_id(hero_id)
print(team.members_by_id)


# Test add_random_member method
new_member = team.manage.add_random_member()
new_member = team.manage.add_random_member()
new_member = team.manage.add_random_member()
new_member = team.manage.add_random_member()
print(team.members_by_id)


# Test 5 maximum members
new_member = team.manage.add_random_member()
new_member = team.manage.add_random_member()
print(team.members_by_id)

print('END: TEAM 1')

print("INIT: TEAM 2")
# Test 6 multiple add by id
a_lot_of_heroes = [1, 30, 25, 38, 200, 400, 500]
team_2 = Team()
team_2.manage.add_multiple_by_id(a_lot_of_heroes)
print(team_2.members_by_id)
team_2.manage.remove_member_by_id(1)
print(team_2.members_by_id)

print("END: TEAM 2")

print("INIT: TEAM 3")
# Test 7 multiple add random
n_of_heroes = 7
team_3 = Team()
team_3.manage.add_multiple_random(n_of_heroes)
print(team_3.members_by_id)
print("END: TEAM 3")



print("INIT: TEAM 4")
# Test 8 Remove by id
a_lot_of_heroes = [1, 30, 25, 38, 200, 400, 500]
team_4 = Team()
team_4.manage.add_multiple_by_id(a_lot_of_heroes)
print(team_4.members_by_id)
print(team_4.members_names)
print(team_4.members)
team_4.manage.remove_member_by_id(1)
team_4.manage.remove_member_by_id(30)
team_4.manage.remove_member_by_id(25)
team_4.manage.remove_member_by_id(38)
print(team_4.members_by_id)
print(team_4.members_names)
print(team_4.members)
print("END: TEAM 4")

# Test 8 Remove all
a_lot_of_heroes = [1, 30, 25, 38, 200, 400, 500]
team = Team()
team.manage.add_multiple_by_id(a_lot_of_heroes)
print(team.members_by_id)
print(team.members_names)
print(team.members)
team.manage.remove_all_members()
print(team.members_by_id)
print(team.members_names)
print(team.members)

# Test 9 create
team = Team()
team.create()
print(team.members_in_training)

# Test 10 create
team = Team()
team.create()
print(team.members_in_training)
print(team.alignment)

# Test 11 fb
team = Team()
team.create()
print("team alignment: ", team.alignment)
team.train.fb()
print(team.members_in_training)

# Test 12 fightStats
team = Team()
team.create()
print("team alignment: ", team.alignment)
team.train.fb()
team.train.fight_stats()

# Test 13 attacks
team = Team()
team.create()
print("team alignment: ", team.alignment)
team.train.fb()
team.train.fight_stats()
team.train.all_attacks()
"""

# Test 14 hp
team = Team()
team.create()
print("team alignment: ", team.alignment)
team.train.fb()
team.train.fight_stats()
team.train.all_attacks()
team.train.hp()
team.train.hp_increment_by_factor(10)
team.train.ready_to_fight()
print(team.members_in_training)

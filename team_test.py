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

"""
print("INIT: TEAM 2")
# Test 6 multiple add by id
a_lot_of_heroes = [1, 30, 25, 38, 200, 400, 500]
team_2 = Team()
team_2.manage.add_multiple_by_id(a_lot_of_heroes)
print(team_2.members_by_id)

print("END: TEAM 2")

print("INIT: TEAM 3")
# Test 7 multiple add random
n_of_heroes = 7
team_3 = Team()
team_3.manage.add_multiple_random(n_of_heroes)
print(team_3.members_by_id)
print("END: TEAM 3")

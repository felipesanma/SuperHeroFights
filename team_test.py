from team import Team

"""
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

"""
# Test multiple add by id
a_lot_of_heroes = [1, 30, 25, 38, 200, 400, 500]
team_2 = Team()
team_2.manage.add_multiple_by_id(a_lot_of_heroes)
print(team_2.members_by_id)

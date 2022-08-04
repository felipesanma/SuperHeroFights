from team import Team

team = Team()


# Test add_member_by_id method
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

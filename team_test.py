from team import Team

team = Team()
hero_id = 1
no_id = 0
new_member = team.manage.add_member_by_id(hero_id)
new_member = team.manage.add_member_by_id(no_id)
print(team.members)

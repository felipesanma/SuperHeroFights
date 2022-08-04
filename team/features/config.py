import json

# Reference: https://akabab.github.io/superhero-api/api/glossary.html
FIRST_HERO_ID = 1
LAST_HERO_ID = 731
black_list_file = open("hero_black_list_id.json")
HERO_BLACKLIST_ID = json.load(black_list_file)["hero_black_list_id"]
ALL_HEROE_ID = list(range(FIRST_HERO_ID, LAST_HERO_ID + 1))
POSSIBLE_HEROE_ID = set(ALL_HEROE_ID) - set(HERO_BLACKLIST_ID)
print(POSSIBLE_HEROE_ID)
# Declared on task
MAX_HERO_MEMBERS = 5

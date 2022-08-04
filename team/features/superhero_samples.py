from superhero import SuperHero

id = 12
superhero = SuperHero(id=id)
superheroe, status_code = superhero.characters.get_complete_information()
print(superheroe.name)

# all_superheroes = superhero.characters.get_all()
# print(all_superheroes)

powerstats, status_code = superhero.powerstats.get()
print(powerstats)


appearance, status_code = superhero.appearance.get()
print(appearance)

biography, status_code = superhero.biography.get()
print(biography)


connections, status_code = superhero.connections.get()
print(connections)

work, status_code = superhero.work.get()
print(work)

size = "sm"
image = superhero.images.get_url_by_size(size=size)
print(image)

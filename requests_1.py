# Задание 1

import requests


def the_most_iintellegence(superheroes):
    heroes_dict = {}
    max_point = 0
    name = None
    for hero in superheroes:
        url = "https://superheroapi.com/api/2619421814940190/search/"
        name = hero
        response = requests.get(url + name, timeout=5)
        intellect = response.json()['results'][0]['powerstats']['intelligence']
        heroes_dict[hero] = intellect
    for key, value in heroes_dict.items():
        if int(value) > max_point:
            max_point = int(value)
            name = key
    # print(key, max_point)

    return f'Самый умнный супергерой {name}! \nЗначение "intelligence" равно {max_point}.'


print(the_most_iintellegence(["Hulk", "Captain America", "Thanos"]))

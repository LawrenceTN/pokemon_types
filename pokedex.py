import pandas as pd
import re

# https://github.com/PokeAPI/pokeapi
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.update.html
# https://www.programiz.com/python-programming/nested-dictionary


pokemon_types = {
    "fire" : 
        {
            "strong" : ["grass", "ice", "bug", "steel"],
            "weak" : ["fire", "water", "rock", "dragon"]
        },
    "normal" :
        {
            "strong" : [],
            "weak" : ["rock", "ghost"]
        },
    "water" :
        {
            "strong" : ["fire", "ground", "rock"],
            "weak" : ["water", "dragon", "grass"]
        },
    "grass" :
        {
            "strong" : ["water", "ground", "rock"],
            "weak" : ["fire", "grass", "poison", "flying", "bug", "dragon", "steel"]
        },
    "electric" :
        {
            "strong" : ["water", "flying"],
            "weak" : ["grass", "electric", "dragon", "ground"]
        },
    "ice" :
        {
            "strong" : ["grass", "ground", "flying"],
            "weak" : ["ice", "fire", "water", "steel"]
        },
    "fighting" :
        {
            "strong" : ["normal", "ice", "rock", "dark", "steel"],
            "weak" : ["poison", "flying", "psychic", "bug", "fairy"]
        },
    "poison" :
        {
            "strong" : ["grass", "fairy"],
            "weak" : ["fighting", "poison", "rock", "ghost", "steel"]
        },
    "ground" :
        {
            "strong" : ["fire", "electric", "poison", "rock", "steel"],
            "weak" : ["grass", "flying", "bug"]
        },
    "flying" :
        {
            "strong" : ["grass", "bug", "fighting"],
            "weak" : ["electric", "rock", "steel"]
        },
    "psychic" :
        {
            "strong" : ["fighting", "poison"],
            "weak" : ["psychic", "dark", "steel"]
        },
    "bug" :
        {
            "strong" : ["grass", "psychic", "dark"],
            "weak" : ["fire", "fighting", "poison", "flying", "ghost", "steel", "fairy"]
        },
    "rock" :
        {
            "strong" : ["fire", "fighting", "flying", "bug"],
            "weak" : ["fighting", "ground", "steel"]
        },
    "ghost" :
        {
            "strong" : ["psychic", "ghost"],
            "weak" : ["normal", "dark"]
        },
    "dragon" :
        {
            "strong" : ["dragon"],
            "weak" : ["fairy", "steel"]
        },
    "dark" :
        {
            "strong" : ["psychic", "ghost"],
            "weak" : ["fighting", "dragon", "fairy"]
        },
    "steel" :
        {
            "strong" : ["ice", "rock", "fairy"],
            "weak" : ["fire", "water", "electric", "steel"]
        },
    "fairy" :
        {
            "strong" : ["fighting", "dragon", "dark"],
            "weak" : ["fire", "poison", "steel"]
        }
}

# ans = input("Please enter a pokemon type: ")

# for index, value in pokemon_types.items():

#     #print(index)
#     #print(f"\t{value['strong']}")
#     #print(f"\t{value['weak']}")
#     if ans in value['strong']:
#         print(f"\n{index} is strong against {ans}")

df = pd.read_json('https://raw.githubusercontent.com/DetainedDeveloper/Pokemon-Data-Scraper/master/pokedex_raw/pokedex_raw.json')

# types = list(df.iloc[1][['types'][0]])
# types = df.loc[df['types'].str.contains('grass')]
# print(types)

# print((df.iloc[0]['types'][0]['name'])) # prints grass
# print((df.iloc[0]['types'][1]['name'])) # prints poison
national_dex = len(df)

# print((df.iloc[4]['types'][0]['name'])) # prints grass
# print((df.iloc[4]['types'][1]['name'])) # prints poison

# print(df.iloc[i]['name']) # prints pokemon info at index [i]

# print(df.loc[0]['types'][0]['name'])

# ask user for type
# scan through all pokemon, and display only the ones that have that type along with what they're strong/weak against

for i in range(10):
    pokemon = df.iloc[i]['name']
    print(pokemon)
    type_1 = (df.loc[i]['types'][0]['name'])
    try:
        type_2 = (df.loc[i]['types'][1]['name'])
    except:
        type_2 = "none"
    print("\tType 1: " + type_1)
    print("\tType 2: " + type_2)

    for values, keys in pokemon_types.items():
        if type_1 or type_2 in pokemon_types.keys():
            print(f"strong against: {pokemon_types[type_1]['strong']}\n")
            break
        
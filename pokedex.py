import pandas as pd

# https://github.com/PokeAPI/pokeapi
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.update.html

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

df = pd.read_json('https://raw.githubusercontent.com/DetainedDeveloper/Pokemon-Data-Scraper/master/pokedex_raw/pokedex_raw.json')

# types = list(df.iloc[1][['types'][0]])
# types = df.loc[df['types'].str.contains('grass')]
# print(types)

# print((df.iloc[0]['types'][0]['name'])) # prints grass
# print((df.iloc[0]['types'][1]['name'])) # prints poison
# print(df.iloc[0]['id']) # prints pokemon info at index [i]

def search():
    poke_type = ""
    poke_type = input("Which pokemon type would you like to view: ")
    national_dex = len(df)

    for i in range(national_dex):
        # Filter the pokemon
        type_1 = (df.loc[i]['types'][0]['name'])
        try:
            type_2 = (df.loc[i]['types'][1]['name'])
        except:
            type_2 = "none"
        poke_types = [type_1, type_2]

        if poke_type in poke_types:
        # Print pokemon stats:     
            pokemon = df.iloc[i]['name']
            index = (df.iloc[i]['id'])
            print(f"#{index}: {pokemon}")
            print("\tType 1: " + type_1)
            print("\tType 2: " + type_2)

            for keys in pokemon_types.keys():
                if type_1 or type_2 in pokemon_types.keys():
                    print(f"strong against: {pokemon_types[type_1]['strong']}")
                    print(f"weak against: {pokemon_types[type_1]['weak']}\n")
                    if type_2 != 'none':
                        print(f"strong against: {pokemon_types[type_2]['strong']}")
                        print(f"weak against: {pokemon_types[type_2]['weak']}\n")                    
                    break

def main():
    while True:
        search()
        answer = input("Press enter to search again or 'q' to quit")
        if answer == 'q':
            print("Good-bye!")
            break

main()

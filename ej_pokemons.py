import requests
import random

url = 'https://pokeapi.co/api/v2/pokemon-species?offset=0&limit=1025'
webContent = requests.get(url)
pokemons = webContent.json()
claves = list(pokemons.keys())
aleatorio = random.randint(0,100)
nombre = pokemons["results"][aleatorio]["name"]
urlP = pokemons["results"][aleatorio]["url"]

request = requests.get(urlP)
pokemon = request.json()
keys = list(pokemon.keys())

def color(nombre):
    return pokemon["color"]["name"]

def generacion(nombre):
    return pokemon["generation"]["name"]

def habitat(nombre):
    return pokemon["habitat"]["name"]

def forma(nombre):
    return pokemon["shape"]["name"]

print(claves)
print(nombre)
print(urlP)
print("----------------------------")
continuar = True
cont = 1
while continuar:
    print("Adivina el pokemon. Tienes 3 intentos.")
    intento = input(f"Intento {cont}:\n")
    if intento == nombre:
        print("¡Enhorabuena!")
        continuar = False
    else:
        cont += 1
        if cont == 2:
            print("Te daré algunas pistas: ")
            print(f"El color del pokemon es: {color(nombre)}")
            print(f"La generación del pokemon es {generacion(nombre)}")
        elif cont == 3:
            print("Sigues sin adivinarlo...")
            print(f"El habitat del pokemon es: {habitat(nombre)}")
            print(f"La forma del pokemon es: {forma(nombre)}")
        else:
            print(f"No lo has conseguido... El pokemon es: {nombre}")
            continuar = False
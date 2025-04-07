import random

import requests

url = 'https://rickandmortyapi.com/api/character/'
pAl = random.randint(1,826)
webContent = requests.get(f"{url}{pAl}")
personaje = webContent.json()
claves = list(personaje.keys())
valores = list(personaje.values())

def estaVivo(personaje):
    if personaje["status"].lower() == "dead":
        return "muerto"
    elif personaje["status"].lower() == "unknown":
        return "desconocido"
    return "vivo"

def especie(personaje):
    return personaje["species"]

def genero(personaje):
    return personaje["gender"]

def origen(personaje):
    return personaje["location"]["name"]

localizacion = valores[6]
loc = localizacion["name"]

def letrasAdivinadas(palabra, letras):
    nueva = ""
    for i in range(len(palabra)):
        if palabra[i] in letras:
            nueva += palabra[i]
        elif palabra[i] == " ":
            nueva += " "
        else:
            nueva += "_"
    return nueva

"""
urllo = valores[6]["url]
localizacionRequest = requests.get(urllo)
localizacion = localizacionRequest.json()
print(f"localizacion: {localizacion["name"]}")
"""
nombreO = personaje["name"].lower()
print(f"[{nombreO}]")
continuar = True
letras = []
print(letrasAdivinadas(nombreO,letras))
while continuar:
    nombre = input("Adivina el nombre del personaje:\n").lower()
    if nombre == nombreO:
        print("¡Enhorabuena!")
        continuar = False
    else:
        for i in range(len(nombre)):
            if nombre[i] == nombreO[i]:
                letras.append(nombre[i])
        print(letrasAdivinadas(nombreO, letras))
        print(f"El personaje está: {estaVivo(personaje)}")
        print(f"La especie del personaje: {especie(personaje)}")
        print(f"El género del personaje es: {genero(personaje)}")
        print(f"El lugar de origen del personaje es: {origen(personaje)}")

print(f"El nombre es: {personaje['name']}")
#hacer el juego del impostor...
#tiene que pedir cantidad de jugadores y despues nombrar a cada uno .
#hacer una lista con la categoria de palabras que quieran .
#despues tiene que empezar el juego y tiene que elegir 
#un importor y mostrar la palabra seleccionada a todos 
#menos al impostor
#tambien no tiene que verse que es el otro jugador 
#tiene que ir mostrando por uno a la vez sin mostrar 
#que fue el que paso antes
#buscar en internet como hacer para que se borre los print 
#de la terminal para que no se vea lo anterior 


import random 
print("Bienvenidos al juego del impostor!")
estado1=False
while estado1==False:
    try:
        cantJugador=int(input("Cantidad de Jugadores: "))
        estado1=True
        break
    except ValueError:
        print("Escribilo en numeros")

nombres=[]

for x in range(cantJugador):
    nombre=input("Dame uno de los nombres: ")
    nombres.append(nombre)


verduras=["brocoli", "lechuga", "remolacha", "tomate", "zapallo", "zapallito"]
palabraSecreta=random.choice(verduras)
impostor=random.choice(nombres)
posicionImpostor=nombres.index(impostor)
nombres.pop(posicionImpostor)

import subprocess
import time
def limpiar_pantalla():
    subprocess.run('cls', shell=True)

for x in nombres:
    print(f"Ahora es el turno de {x}")
    time.sleep(3)
    print(f"La palabra es: {palabraSecreta}")
    time.sleep(3)
    limpiar_pantalla()


print(f"Ahora es el turno de {impostor}: ")
time.sleep(3)
print(f"¡Sos el impostor! Suerte adivinando")
time.sleep(3)
limpiar_pantalla()

import os
import time
import random 

def limpiar_pantalla():
    os.system('clear')

estado1 = False
while estado1 == False:
    try:
        cantJugador = int(input("Cantidad de Jugadores: "))
        if cantJugador>15 or cantJugador<3:
            print("Elije otro numero")
        else:
            estado1 = True
    except ValueError:
        print("Escribilo en numeros")

nombres = []
for x in range(cantJugador):
    nombre = input("Dame uno de los nombres: ")
    nombres.append(nombre)

verduras = ["brocoli", "lechuga", "remolacha", "tomate", "zapallo", "zapallito"]
palabraSecreta = random.choice(verduras)
impostor = random.choice(nombres)

posicionImpostor = nombres.index(impostor)
nombres.pop(posicionImpostor)

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

nombres.append(impostor)

print("\n--- ¡SALA DE VOTACIÓN SECRETA! ---")
print("Pasen a la computadora a votar uno por uno.\n")

votos = {jugador: 0 for jugador in nombres}
total_jugadores = len(nombres)

for x in range(total_jugadores):
    print(f"Le toca votar al Jugador #{x + 1}...")
    print("Opciones disponibles:")
    
    for indice, jugador in enumerate(nombres):
        print(f"[{indice}] Votar a {jugador}")
        
    voto_valido = False
    while not voto_valido:
        try:
            opcion = int(input("\nIngresa el NÚMERO de tu voto: "))
            if 0 <= opcion < len(nombres):
                jugador_votado = nombres[opcion]
                votos[jugador_votado] += 1
                voto_valido = True
                print("¡Voto registrado en secreto!")
                time.sleep(1.5)
                limpiar_pantalla()
            else:
                print("Ese número no está en la lista. Intentá de nuevo.")
        except ValueError:
            print("Por favor, escribilo en números.")

mas_votado = max(votos, key=votos.get)

print("========================================")
print("       RECUENTO FINAL DE VOTOS          ")
print("========================================")
time.sleep(1)

for jugador, cantidad in votos.items():
    print(f" - {jugador}: {cantidad} voto(s)")
print("----------------------------------------")
time.sleep(2)

if mas_votado == impostor:
    print(f"El jugador más votado de la ronda fue: {mas_votado}")
    print(f"¡VICTORIA! Los tripulantes descubrieron al impostor.")
else:
    print(f"El jugador más votado fue: {mas_votado} y era INOCENTE...")
    print(f"¡DERROTA! El impostor era {impostor} y los engañó a todos.")
print("========================================")

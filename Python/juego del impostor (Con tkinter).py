import random 
import tkinter as tk
from tkinter import messagebox

estado1 = False
while estado1 == False:
    try:
        cantJugador = int(input("Cantidad de Jugadores: "))
        estado1 = True
        break
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

import os
import time
def limpiar_pantalla():
    os.system('clear')

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

ventana = tk.Tk()
ventana.title("¡Bienvenidos al juego del Impostor!")
ventana.geometry("400x400")

texto = tk.Label(ventana, text="Pasen a votar en secreto uno por uno:", font=("Arial", 14))
texto.pack(pady=20) 

votos = {jugador: 0 for jugador in nombres}
votos_totales = 0
total_jugadores = len(nombres)

def votar_jugador(nombre_elegido):
    global votos_totales
    
    votos[nombre_elegido] += 1
    votos_totales += 1
    
    messagebox.showinfo("Voto Registrado", "¡Voto guardado! Que pase el siguiente jugador.")
    
    if votos_totales == total_jugadores:
        mas_votado = max(votos, key=votos.get)

        if mas_votado == impostor:
            messagebox.showinfo("¡VICTORIA!", f"El más votado fue {mas_votado}.\n\n¡Felicidades, descubrieron al impostor!")
        else:
            messagebox.showinfo("DERROTA", f"El más votado fue {mas_votado} y era inocente...\n\nEl impostor era {impostor}. ¡Ganó la partida!")
            
        ventana.destroy()

for x in nombres:
    boton_votar = tk.Button(
        ventana, 
        text=f"Votar a {x}",                              
        command=lambda jugador=x: votar_jugador(jugador), 
        bg="red", 
        fg="white"
    )
    boton_votar.pack(pady=5)

ventana.mainloop()

maquina="piedra"
estado=False
while estado==False:
    try:
        persona=input("Elegi piedra, papel o tijera: ")
        estado=True
        break
    except ValueError:
        print("Elegi bien")
if persona=="piedra":
    print("Empataste")
elif persona=="papel":
    print("Ganaste")
else:
    print("Perdiste")
maquina="piedra"
estado=False
while estado==False:
    try:
        persona=input("Elegi piedra, papel o tijera: ")
        estado=True
        break
    except ValueError:
        print("Error")
if persona=="piedra":
    print("Empataste")
elif persona=="papel":
    print("Ganaste")
elif persona=="tijera":
    print("Perdiste")
else:
    print("Error")
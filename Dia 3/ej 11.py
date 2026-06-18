def puedeVotar(edad):
    if edad>=18:
        return "Puede votar"
    else:
        return "Aun no puede votar"
estado=False
while estado==False:
    try:
        edadN=int(input("Decime tu edad: "))    
        estado=True
        break
    except Exception:
        print("NUmero")


print(puedeVotar(edadN))
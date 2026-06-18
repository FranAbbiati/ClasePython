estado=False
while estado==False:
    try:
        nombreCiudad=input("Dame el nombre de la ciudad donde naciste: ")
        nombreMascota=input("Dame el nombre de tu mascota")
        estado=True
        break
    except Exception:
        print("Responde bien")
print(f"El nombre de tu banda es: {nombreCiudad} {nombreMascota}")
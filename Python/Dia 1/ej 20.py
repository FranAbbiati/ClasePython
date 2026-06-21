estado=False
while estado==False:
    try:
        nombre=input("¿Cual es tu nombre?: ")
        ciudad=input("¿Cual es tu ciudad de origen?: ")
        estado=True
    except ValueError:
        print("Error")

print(f"Hola {nombre}, bienvenido a {ciudad}. ¡Espero que disfrutes el curso!")
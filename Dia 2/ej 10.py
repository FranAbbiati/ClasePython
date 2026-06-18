contraseniaCorrecta="hola123"
respuesta=input("deci la contraseña: ")
while respuesta != contraseniaCorrecta:
    respuesta=input("deci la contraseña: ")
    if respuesta==contraseniaCorrecta:
        break
print("¡Bienvenido!")
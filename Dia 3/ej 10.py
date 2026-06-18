def crearEmail(nombre, apellido):
    return(f"{nombre}.{apellido}@empresa.com")
    

nombreT=input("Decime tu nombre: ")
apellidoT=input("Decime tu apellido: ")

print(f"Tu mail es: {crearEmail(nombreT, apellidoT)}")
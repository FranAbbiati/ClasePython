saldo=1000
estado=True

def verificarPin(pinIngresado):
    if pinIngresado=="1234":
        return(True)
    else:
        return(False)


def retirar(cantidad):
    if cantidad<saldo or cantidad==saldo:
        resta=saldo-cantidad
        return(f"Retiro con exito: {resta}")
    else:
        return("Fondos insuficientes")

print("Bienvenido al banco de python!")

contrasenia=input("Cual es la contraseña: ")
while verificarPin(contrasenia)==False:
    contrasenia=input("Cual es la contraseña: ")
    print(verificarPin(contrasenia))
    if verificarPin(contrasenia)==True:
        break

while estado==True:
    try:
        if verificarPin(contrasenia)==True:
            retiro=int(input("Decime cuanto queres retirar: "))
            print(retirar(retiro))
            estado==False
            break
    except ValueError:
        print("Decimelo en NUMEROS")
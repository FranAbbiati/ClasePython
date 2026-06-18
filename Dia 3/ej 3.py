def cuadrado(numero):
    resultado=numero*numero
    return resultado
estado=False
while estado==False:
    try:
        numN=float(input("Deci un numero: "))
        estado=True
        break
    except ValueError:
        print("Dame numero")

print(cuadrado(numN))
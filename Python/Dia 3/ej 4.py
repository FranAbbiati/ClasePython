def esPar(numero):
    if numero%2==0:
        return True
    else:
        return False
estado=False
while estado==False:
    try:
        numN=int(input("Decime un numero"))
        estado=True
        break
    except Exception:
        print("NUmero")
print(esPar(numN))
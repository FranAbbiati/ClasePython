import random

secreto= random.randint(1,100)
adivinado=False
estado=False
print("pense un numero del 1 al 100, adivinalo. ")
while adivinado==False:
    while estado==False:
        try:
            intentoN=int(input("Elegi un numero: "))
            estado=True
            break
        except Exception:
            print("Dame numero entero")
    if intentoN==secreto:
        adivinado=True
        print("Ganaste")
    elif intentoN>secreto:
        print("Mas chico")
    else:
        print("Es mas grande")
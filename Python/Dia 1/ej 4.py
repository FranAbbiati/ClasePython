estado=False

while estado==False:
        try:
            baseT=input("Dame la base de un rectangulo: ")
            baseN=float(baseT)

            alturaT=input("Dame la altura del rectangulo: ")
            alturaN=float(alturaT)
            estado=True
            break
        except ValueError:
            print("Dame NUMEROS")
area=baseN*alturaN

print(f"El area del rectangulo es {area}")
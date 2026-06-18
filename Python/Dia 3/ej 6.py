def areaCirculo(radio):
    formula=3.1416*radio*radio
    return formula
estado=False
while estado==False:
    try:
        radioN=float(input("Decime el radio del circulo: "))
        estado=True
        break
    except Exception:
        print("Dame un numero")

print(f"El area del circulo es {areaCirculo(radioN)}")
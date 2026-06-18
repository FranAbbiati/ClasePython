def temperatura(grados):
    formula=(gradosCN*9/5)+32
    return formula

estado=False
while estado==False:
    try:
        gradosCN=float(input("Decime los grados celsius: "))
        estado=True
        break
    except Exception:
        print("Dame un numero")

print(f"La temperatura en Farenheit es {temperatura(gradosCN)}")
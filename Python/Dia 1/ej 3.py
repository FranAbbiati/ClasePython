estado=False

while estado==False:
    try:
        dolarT=input("¿Cuantos dolares tenes?")
        dolarN=float(dolarT)
        estado=True
    except ValueError:
        print("Dame NUMEROS")

pesos=dolarN*1000

print(f"Tenes {pesos} pesos")
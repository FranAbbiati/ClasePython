estado=False

while estado==False:
    try: 
            totalCuentaT=input("¿Cual es el total?")
            totalCuentaN=float(totalCuentaT)
            PropinaPorT=input("¿Cuanto queres dejar?")
            PropinaPorN=float(PropinaPorT)
            estado=True
            break
    except ValueError:
        print("Dame NUMEROS: ")


Propina=PropinaPorN*totalCuentaN/100
totalPagar=Propina+totalCuentaN

print(f"Esta es la propina:{Propina} Este es el total {totalPagar}")
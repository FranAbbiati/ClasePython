estado=False
while estado==False:
    try:
        cantidadDiasT=input("Dame una cantidad de dias: ")
        cantidadDiasN=float(cantidadDiasT)
        esto=True
        break
    except Exception:
        print("Dame NUMEROS")
segundos=cantidadDiasN*24*60*60

print(f"En segundos es {segundos}")
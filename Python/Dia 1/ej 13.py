estado=False
while estado==False:
    try:
        notaT=input("Dame la nota: ")
        notaN=float(notaT)
        estado=True
        break
    except Exception:
        print("Dame numeros")
if notaN>=6:
    print(f"Aprobado")
else:
    print(f"Desaprobado")
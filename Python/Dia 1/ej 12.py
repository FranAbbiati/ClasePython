estado=False
while estado==False:
    try:
        numT=input("Dame un numero: ")
        numN=float(numT)
        estado=True
        break
    except Exception:
        print("Dame numero")
if numN>0:
    print(f"Es positivo")
elif numN==0:
    print(f"Es igual a cero")
else:
    print(f"Es negativo")
    
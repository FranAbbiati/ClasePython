estado=False
while estado==False:
    try:
        num1T=input("Dame un numero: ")
        num1N=float(num1T)

        num2T=input("Dame un numero: ")
        num2N=float(num2T)
        estado=True
        break
    except Exception:
        print("Dame NUMEROS")
if num1N>num2N:
    print(f"El numero mayor es {num1N}")
elif num1N==num2N:
    print(f"Son iguales")
else:
    print(f"El numero mayor es {num2N}")
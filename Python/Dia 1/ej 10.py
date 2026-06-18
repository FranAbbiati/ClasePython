estado=False
while estado==False:
    try:
        num1T=input("Dame un numero: ")
        num1N=int(num1T)

        num2T=input("Dame un numero: ")
        num2N=int(num2T)
        estado=True
        break
    except Exception:
        print("Dame Numeros")
if num2N==0:
    print("Error")
else:
    division=num1N/num2N
    print(f"El {num1N} dividido {num2N} da {division}")
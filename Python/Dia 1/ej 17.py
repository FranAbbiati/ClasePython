estado=False
while estado==False:
    try:
        pesoT=input("Dame tu peso: ")
        pesoN=float(pesoT)

        alturaT=input("Dame tu altura: ")
        alturaN=float(alturaT)
        estado=True
        break
    except Exception:
        print("Dame numeros")
imc=pesoN/(alturaN*alturaN)

print(f"El IMC es: {imc}")
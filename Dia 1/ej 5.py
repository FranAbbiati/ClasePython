estado=False
while estado==False:
    try:
        nota1T=input("Dame una nota: ")
        nota1N=float(nota1T)

        nota2T=input("Dame una nota: ")
        nota2N=float(nota2T)

        nota3T=input("Dame una nota: ")
        nota3N=float(nota3T)
        estado=True
        break
    except ValueError:
        print("Dame NUMEROS")
promedio=(nota1N+nota2N+nota3N)/3
print(f"tu promedio es: {promedio}")
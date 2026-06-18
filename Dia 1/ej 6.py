estado=False

while estado==False:
    try:
        gradosCT=input("Dame la temperatura en grados celcius: ")
        gradosCN=float(gradosCT)
        estado=True
        break
    except ValueError:
        print("Dame NUMEROS")
gradosF=(gradosCN*9/5)+32

print(f"La temperatura en grados Fahrenheit es {gradosF}")
def mayorDeTres(n1, n2, n3):
    if n1>n2 and n1>n3:
        return n1
    elif n2>n1 and n2>n3:
        return n2
    elif n3>n1 and n3>n2:
        return n3
    else:
        print("No hay un solo numero mayor")
estado=False
while estado==False:
    try:    
        n4=int(input("Dame un numero: "))
        n5=int(input("Dame un numero: "))
        n6=int(input("Dame un numero: "))
        estado=True
        break
    except Exception:
        print("DAme numero")
print(f"El numero mayor es: {mayorDeTres(n4, n5, n6)}")
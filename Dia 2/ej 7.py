sumaTot=0
numN=1
estado=False
while numN!=0:
    while estado==False:
        try:
            numN=int(input("Dame un numero: "))
            estado=True
            break
        except ValueError:
            print("dame un  numero")
    sumaTot=sumaTot+numN
    if numN==0:
        break
print(sumaTot)
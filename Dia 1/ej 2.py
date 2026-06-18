estado=False
while estado==False: 
    try:
        numIntTexto=input("Dame un numero entero: ")
        numINtNumero=int(numIntTexto)
        estado=True
        break
    
    except ValueError:
        print("Dame NUMEROS")
cuenta=numINtNumero%2

if cuenta ==0:
    print("Es par")
else:
    print ("ES impar")    
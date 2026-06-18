anioActual=2026
estado=False
while estado==False:
    try:
        anioNumero=int(input("¿Cual es tu año de nacimiento?: "))
        estado=True
        break
    except ValueError:
        print("Dame Numero")
edad=anioActual-anioNumero

if edad >=18:
    print("Eres mayor de edad, puedes pasar")
else:
    print("Eres menor de edad, no puedes pasar") 



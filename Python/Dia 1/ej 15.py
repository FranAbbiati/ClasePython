estado=False
while estado==False:
    try:
        luz=input("Dame la luz del semaforo")
        estado=True
        break
    except ValueError:
        print("Decime: verde, amarillo o rojo")
if luz=="verde":
    print("Avanzar")
elif luz=="amarillo":
    print("Precaucion")
elif luz=="rojo":
    print("Detenerse")
else:
    print("Error")
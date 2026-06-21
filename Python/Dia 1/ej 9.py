estado=False
while estado==False:
    try:
        precioOT=input("Dame el precio original: ")
        precioON=float(precioOT)

        descuentoT=input("Dame el descuento: ")
        descuentoN=float(descuentoT)
        estado=True
        break
    except Exception:
        print("Dame Numeros")
montodes=precioON*descuentoN/100
precioF=precioON-montodes

print(f"El precio final es {precioF}")
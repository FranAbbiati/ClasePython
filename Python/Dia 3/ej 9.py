def calcularPrecioFinal(precio, descuento):
    precioFinal=precio-descuento
    return precioFinal
estado=False
while estado==False:
    try:
        precioN=float(input("Decime el precio: "))
        descuentoN=float(input("Decime el descuento: "))
        estado=True
        break
    except Exception:
        print("Dame numeros")
descuentoR=descuentoN*100/precioN

print(f"El precio final es {calcularPrecioFinal(precioN,descuentoR)}")
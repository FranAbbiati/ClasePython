precios={
    "manzana" : 100,
    "banana" : 50,
    "naranja" : 80
}
estado=False
while estado==False:
    try:    
        frutaPedida=input("decime una fruta: ")
        kilosN=float(input("Decime cantidad de kilos: "))
        estado=True
        break
    except Exception:
        print("Lee")
if frutaPedida=="manzana":
    precioTot=precios.get("manzana")*kilosN
elif frutaPedida=="naranja":
    precioTot=precios.get("naranja")*kilosN
elif frutaPedida=="banana":
    precioTot=precios.get("banana")*kilosN

print(f"el precio total es: {precioTot}")
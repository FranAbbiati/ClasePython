estado=False
while estado==False:
    try:
        horasMesT=input("¿Cuantas horas trabajaste este mes?")
        horasMesN=float(horasMesT)

        tarifaHT=input("dame la tarifa por hora: ")
        tarifaHN=float(tarifaHT)
        estado=True
        break
    except Exception:
        print("Dame Numeros")
salario=horasMesN*tarifaHN

print(f"El salario es {salario}")
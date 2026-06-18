def min_horas(minutos):
    hours=minutos//60
    minutes=(minutos-(hours*60))
    return (f"{hours} horas y {minutes} minutos")

estado=False
while estado==False:
    try:
        minutosN=int(input("Decime los minutos: "))
        estado=True
        break
    except Exception:
        print("Dame numero")

print(min_horas(minutosN))
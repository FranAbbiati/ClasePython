agenda= {
    "Juana": "01234567",
    "Juan": "23456789",
    "Jose": "98765432"
}
estado=False
while estado==False:
    try:
        ingreso=input("Dame un nombre: ")
        if ingreso=="Juana":
            print("EL numero de Juana es: ", agenda["Juana"])
        elif ingreso=="Jose":
            print("El numero de Jose es: ", agenda["Jose"])
        elif ingreso=="Juan":
            print("El numero de Juan es: ", agenda["Juan"])
        else:
            print("No esta esa persona agendada")
        estado=True
        break
    except Exception:
        print("Dame una palabra")
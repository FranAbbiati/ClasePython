estado=False
while estado==False:
   try:
      numeroN=int(input("Dame un numero: "))
      estado=True
      break
   except Exception:
      print("Dame un numero")
valor1=0
for numero in range (1, 11):
   valor1=valor1+1
   mult=valor1*numeroN
   print(f"{numeroN} por {valor1} = {mult}")
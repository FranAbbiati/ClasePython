estado=False
while estado==False:
  try:
    frase=input("Dame una frase: ")
    estado=True
    break
  except Exception:
   print("Dame una frase")
cont=0
for letra in frase:
    if letra in "aeiouAEIOU":
      cont=cont+1  
print(f"El total de vocales es {cont}")
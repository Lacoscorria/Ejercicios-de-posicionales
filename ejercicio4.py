edad = int(input("ingrese edad:"))
licencia = input("ingrese la licencia si/no):").lower()
if edad >=18 and licencia == "si":
    print("esta preparado para conducir")
else:
    print("no esta preparado para conducir")
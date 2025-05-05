# Solicitar la edad al usuario
edad = int(input("Ingrese su edad: "))

# Clasificar según el rango de edad
if edad < 10:
    print("Es un niño.")
elif edad >= 10 and edad < 15:
    print("Es un preadolescente.")
elif edad >= 15 and edad < 18:
    print("Es un adolescente.")
elif edad >= 18 and edad <= 50:
    print("Es un adulto.")
else:
    print("Es un adulto mayor.")
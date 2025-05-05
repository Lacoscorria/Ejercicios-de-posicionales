nombre1 = input("Ingrese el nombre del primer hermano: ")
edad1 = int(input("Ingrese la edad del primer hermano: "))

# Solicitar datos del segundo hermano
nombre2 = input("Ingrese el nombre del segundo hermano: ")
edad2 = int(input("Ingrese la edad del segundo hermano: "))

# Comparar las edades y determinar quién es el mayor
if edad1 > edad2:
    print("El hermano mayor es:", nombre1)
elif edad2 > edad1:
    print("El hermano mayor es:", nombre2)
else:
    print("Ambos hermanos tienen la misma edad.")
edad = int(input("Ingrese su edad: "))
carnet = input("¿Usted tiene carnet de conducir? (si/no):")
if edad >=18 and carnet == "si":
    print("Usted puede alquilar y conducir el auto.")
elif edad >=18 and carnet == "no":
    print("Usted puede alquilar el auto pero no puede conducirlo.")
else:
    print("Usted no puede alquilar ni conducir el auto.")
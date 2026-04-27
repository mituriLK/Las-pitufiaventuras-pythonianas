print("=== CALCULADORA DE PROPINA ===")
nombre = input("Ingrese su nombre: ")
cuenta = float(input("Ingrese el monto final de su cuenta: "))
porcentaje = float(input("Ingrese cuanta propina va a dejar: "))
division = str(input("¿La cuenta es para dos o más personas?: "))
if division == "si":
    personas = int(input("Ingrese para cuantas personas: "))
else:
    print("Cargando datos...")
propina = cuenta * (porcentaje/100)
total = cuenta + propina
if division == "si":
    total_personas = total / personas
    if total <100000:
        print("Cargando datos...")
    elif total >=100000:
        cuotas_og = str(input("¿Desea pagar en cuotas? (si/no): "))
        if cuotas_og == "si":
            print("\n 3 cuotas(sin interes) | 6 cuotas | 9 cuotas | 12 cuotas")
            cuotas = int(input("Introduzca por cuantas cuotas va a pagar: "))
            print("¡Excelente,"+nombre+"! Vaya a recepción para realizar el pago en cuotas con su tarjeta.")

else:
    print("Si desea cambiar su elección y pagar en cuotas puede ir a recepción.")

print("=== TICKET DE",nombre,"===")
print("Bienvenido/a,",nombre+"!")
print("Cuenta: $",cuenta)
print("Propina: %",porcentaje)
print("Total: $",total)
if division == "si":
    print("Total para c/u: $",total_personas)
    if total >= 100000:
        print("Total en cuotas: $",total+(total/cuotas))
    else:
        print("...")
print("=== GRACIAS POR SU COMPRA! ===")


if porcentaje >=20:
    print("¡Excelente! Usted es muy generoso, ¡siga así!")
elif porcentaje >=15:
    print("¡Buena propina, muchas gracias!")
elif porcentaje >= 10:
    print("Gracias por su propina.")
else:
    print("¡Podria ser un poco mas genoroso!")
print("=== CALCULADORA DE CUENTA + PROPINA ===\n")


nombre = input("Ingrese su nombre: ")
cuenta = float(input("Ingrese el monto de la cuenta: $"))
porcentaje_propina = float(input("¿Qué porcentaje de propina desea dejar? (ej: 10, 15, 20): "))


propina = cuenta * (porcentaje_propina / 100)
total = cuenta + propina


es_grupal = input("\n¿La cuenta es para varias personas? (si/no): ").strip().lower()

if es_grupal == "si":
    personas = int(input("¿Cuántas personas son?: "))
    total_por_persona = total / personas
else:
    personas = 1
    total_por_persona = total


print("" + "="*40)
print("RESUMEN DE LA CUENTA")
print("="*40)
print(f"Cliente: {nombre}")
print(f"Monto de la cuenta: ${cuenta:.2f}")
print(f"Propina ({porcentaje_propina}%): ${propina:.2f}")
print(f"Total a pagar: ${total:.2f}")
print(f"Total por persona: ${total_por_persona:.2f}")


if porcentaje_propina >= 20:
    print("¡Excelente! Sos muy generoso")
elif porcentaje_propina >= 15:
    print("¡Buena propina! Muchas gracias")
elif porcentaje_propina >= 10:
    print("Gracias por dejar propina.")
else:
    print("La próxima vez podrías ser un poco más generoso")


if total >= 50000:
    pagar_cuotas = input("¿Desea pagar en cuotas? (si/no): ").strip().lower()
    
    if pagar_cuotas == "si":
        print("Opciones disponibles: 3 | 6 | 9 | 12 cuotas")
        cuotas = int(input("¿En cuántas cuotas quiere pagar?: "))
        
        if cuotas in [3, 6, 9, 12]:
            monto_por_cuota = total / cuotas
            print(f"Perfecto! Pagará ${monto_por_cuota:.2f} por mes durante {cuotas} meses.")
        else:
            print("Lo siento, esa cantidad de cuotas no está disponible.")
    else:
        print("Perfecto, pago al contado disponible.")
else:
    print("Para pagos en cuotas el total debe ser mayor a $50.000")

print("" + "="*40)
print("¡GRACIAS POR COMER CON NOSOTROS!")
print("="*40)
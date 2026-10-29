print("Museo de Antropología e Historia")

# Validar la edad
while True:
    edad = int(input("Escribe tu edad: "))

    if edad < 0 or edad > 110:
        print("Edad no válida. Intenta de nuevo.")
    else:
        break

# Calcular precio
if edad < 3:
    precio = 0
elif edad < 18:
    precio = 30
else:
    precio = 45

# Descuento por edad
if edad >= 60 and precio > 0:
    precio *= 0.88
    print("Tienes un descuento del 12% por edad.")

# Tipo de visitante
print("¿Qué tipo de visitante eres?")
print("a) Estudiante")
print("b) Profesor")
print("c) Adulto mayor")
print("d) Ninguno")

tipo_visitante = input("Ingresa a, b o c: ").lower()

if tipo_visitante == "a" or tipo_visitante == "b":
    precio *= 0.10
    print("Se aplica un descuento del 10% por tu tipo de visitante")
elif tipo_visitante == "c":
    precio *= 0.12
    print("No tienes descuento por tipo de visitante.")
else:
    print("Tipo de visitante no válido.")
    print("si eres menor de 18 no tienes descuento")
#if edad < 18 :
  #  print("no aplica descuento ")
#if edad > 60 :
 #   print("solo un descuento, el mayor")

else: 
 #   print(f"El precio final es: ${precio}")

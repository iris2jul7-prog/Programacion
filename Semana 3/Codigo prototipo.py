# Prototipo  - Sistema de Registro de Citas
precio_fisio = 400
precio_deportiva = 400
precio_sanacion = 400
precio_electro= 300

citas = 0
opcion = 0

print("=== Centro de Fisioterapia y Sanación ===")
print("Sistema de Registro de Citas")

while opcion != 3:
    print()
    print("------ MENÚ ------")
    print("1. Registrar atención")
    print("2. Ver catálogo de servicios")
    print("3. Salir")
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        # Nombre
        nombre = input("Nombre del paciente: ")
        while nombre == "":
            print("El nombre no puede estar vacío.")
            nombre = input("Nombre del paciente: ")

        # Teléfono
        telefono = input("Teléfono (10 dígitos): ")
        while len(telefono) != 10:
            print("El teléfono debe tener 10 dígitos.")
            telefono = input("Teléfono (10 dígitos): ")

        # Edad
        edad = int(input("Edad: "))
        while edad < 1 or edad > 110:
            print("Edad no válida.")
            edad = int(input("Edad: "))

        # Servicio
        print("1) Fisioterapia general  2) Rehabilitación deportiva")
        print("3) Terapia de sanación   4) Electroterapia")
        servicio = int(input("Servicio (1-4): "))
        while servicio < 1 or servicio > 4:
            print("Servicio no válido.")
            servicio = int(input("Servicio (1-4): "))

        if servicio == 1:
            nombre_servicio = "Fisioterapia general"
        elif servicio == 2:
            nombre_servicio = "Rehabilitación deportiva"
        elif servicio == 3:
            nombre_servicio = "Terapia de sanación"
        else:
            nombre_servicio = "Electroterapia"

        # Día
        print("1) Lunes 2) Martes 3) Miércoles 4) Jueves 5) Viernes ")
        dia = int(input("Día de la cita (1-5): "))
        while dia < 1 or dia > 5:
            print("Solo se atiende de lunes a sábado.")
            dia = int(input("Día de la cita (1-5): "))

        if dia == 1:
            dia = "Lunes"
        elif dia == 2:
            dia = "Martes"
        elif dia == 3:
            dia = "Miércoles"
        elif dia == 4:
            dia = "Jueves"
        elif dia == 5:
            dia = "Viernes"
        

        # Hora
        hora = int(input("Hora de la cita (11 a 21): "))
        while hora < 11 or hora > 21:
            print("El horario es de 11 a 21.")
            hora = int(input("Hora de la cita (11 a 21): "))
        hora_fin = hora + 1

        # Primera vez
        respuesta = input("¿Es paciente de primera vez? (si/no): ")
        while respuesta != "si" and respuesta != "no":
            respuesta = input("Escribe si o no: ")
        primera_vez = respuesta == "si"

        # Proceso
        adulto_mayor = edad >= 60
        citas = citas + 1

        # Salida
        print()
        print("--- Detalles de la cita", citas, "---")
        print("Paciente:", nombre)
        print("Teléfono:", telefono)
        print("Edad:", edad, "años")
        print("Servicio:", nombre_servicio)
        print("Día:", dia)
        print("Horario:", str(hora) + ":00 a " + str(hora_fin) + ":00")
        if primera_vez:
            print("Nota: Primera vez. Llegar 15 minutos antes.")
        print("Cita registrada.")

    elif opcion == 2:
        print()
        print("--- Catálogo de servicios ---")
        for i in range(1, 5):
            if i == 1:
                print(i, "Fisioterapia general: $", precio_fisio)
            elif i == 2:
                print(i, "Rehabilitación deportiva: $", precio_deportiva)
            elif i == 3:
                print(i, "Terapia de sanación: $", precio_sanacion)
            else:
                print(i, "Electroterapia: $", precio_electro)
        print("Tu cita es a las : lunes a sábado de 11:00 a 21:00")

    elif opcion == 3:
        print("Hasta luego.")

    else:
        print("Opción no válida.")


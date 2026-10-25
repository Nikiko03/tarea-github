
# Curso: Fundamentos de Tecnología Digitales.
# Profesor: Adonis Aleman G.
# Estudiante: Nicole Tatiana Solórzano Martinez.



cantidad_turnos = 2
estaciones = 3
max_alerta = 8.5

turnos = ["Mañana", "Noche"]

reporte = ""

for turno in range(cantidad_turnos):

    nombre = turnos[turno]
    
    reporte += "\nTurno: {}\n".format(nombre)

    estacion = 0

    while estacion < estaciones:

        valido = False

        while not valido:

            try:
                peso = float(input(
                    "Ingrese la merma de la estación {} del turno {}: "
                    .format(estacion + 1, nombre)
                ))

                if peso < 0:
                    print("ADVERTENCIA: Peso no puede ser negativo")
                else:
                    valido = True

            except ValueError:
                print("ALERTA: Entrada inválida\n El dato ingresado problablemete no es numerico")

        if peso > max_alerta:
            alerta= (" ALERTA: Revisar merma, exceso de peso")
        else:
            alerta =("")

        reporte += "\tEstación {}: {:.1f} kg{}\n".format(
            estacion + 1, peso, alerta
        )

        estacion += 1

print("=======Reporte Final=======")
print(reporte)
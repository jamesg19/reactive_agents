# Definición de estados, percepciones, reglas, acciones y modelo
estados = ["espera-en-A", "espera-en-B", "sucio-A", "sucio-B"]
#Percepcciones de la aspiradora
percepciones = ["limpio", "sucio", "A", "B"]
# estados:regla
reglas = {
    "espera-en-A": "no-limpia-en-A",
    "espera-en-B": "no-limpia-en-B",
    "sucio-B": "limpiar-B",
    "sucio-A": "limpiar-A"
}
# reglas:acciones
acciones = {
    "no-limpia-en-A": "nada",
    "no-limpia-en-B": "nada",
    "limpiar-B": "limpiar-B",
    "limpiar-A": "limpiar-A"
}
# Definir el modelo
#   { Estado, reglas, percepcion }: Estado
modelo = {
    ("espera-en-A", "no-limpia-en-A", "limpio"): "espera-en-B",
    ("espera-en-A", "no-limpia-en-A", "sucio"): "sucio-A",
    ("espera-en-B", "no-limpia-en-B", "limpio"): "espera-en-A",
    ("espera-en-B", "no-limpia-en-B", "sucio"): "sucio-B",
    ("sucio-A", "limpiar-A", "sucio"): "espera-en-B",
    ("sucio-B", "limpiar-B", "sucio"): "espera-en-A",
    ("sucio-A", "limpiar-A", "limpio"): "espera-en-B",
    ("sucio-B", "limpiar-B", "limpio"): "espera-en-A",

}


# Función para actualizar el estado según la percepción
def actualizar_estado(estado, accion, percepcion):
    print("Estado: ",estado," Accion: ",accion," Percepcion: ",percepcion)

    if (estado, accion, percepcion) in modelo:
        return modelo[(estado, accion, percepcion)]
    else:
        return "limpio"


# Programa principal del agente
estado = "espera-en-A"
accion = "no-limpia-en-A"
while True:
    print("Estado: ", estado)
    print("Accion: ", accion)
    percepcion = input("Ingrese percepción: ")  # Se simula la percepción aquí

    estado = actualizar_estado(estado, accion, percepcion)
    accion = reglas[estado]
    print("Estado: ",estado)
    print("Acción: ", acciones[accion])
    print("\n\n\n")

import tkinter as tk

# Definición de estados, percepciones, reglas, acciones y modelo
estados = ["espera-en-A", "espera-en-B", "sucio-A", "sucio-B"]

# Percepciones de la aspiradora
percepciones = ["limpio", "sucio", "A", "B"]

# Estados: Regla
reglas = {
    "espera-en-A": "no-limpia-en-A",
    "espera-en-B": "no-limpia-en-B",
    "sucio-B": "limpiar-B",
    "sucio-A": "limpiar-A"
}

# Reglas: Acciones
acciones = {
    "no-limpia-en-A": "nada",
    "no-limpia-en-B": "nada",
    "limpiar-B": "limpiar-B",
    "limpiar-A": "limpiar-A"
}

# Definir el modelo
#   { Estado, reglas, percepción }: Estado
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
    print("Estado: ", estado, " Accion: ", accion, " Percepcion: ", percepcion)

    if (estado, accion, percepcion) in modelo:
        return modelo[(estado, accion, percepcion)]
    else:
        return "limpio"


# Función para manejar la entrada del usuario
def handle_input():
    global estado
    global accion

    percepcion = entry.get()  # Obtener la percepción del usuario

    estado = actualizar_estado(estado, accion, percepcion)
    accion = reglas[estado]

    state_label.config(text="Estado: " + estado)
    action_label.config(text="Acción: " + acciones[accion])


# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Interfaz de Aspiradora")

state_label = tk.Label(root, text="Estado: ")
state_label.pack()

action_label = tk.Label(root, text="Acción: ")
action_label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Enviar Percepción", command=handle_input)
button.pack()

root.mainloop()

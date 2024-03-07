# Definir los estados, percepciones, reglas y acciones
estados = ['sin-moneda', 'recibi-moneda', 'servido-c1', 'servido-c2', 'servido-c3']
percepciones = ['moneda', 'c1', 'c2', 'c3', 'servido']
# estados:regla
reglas = {
    "sin-moneda": "pedir-moneda",
    "recibi-moneda": "pedir-codigo",
    "servido-c1": "servir-c1-esperar",
    "servido-c2": "servir-c2-esperar",
    "servido-c3": "servir-c3-esperar"
}
# reglas:acciones
acciones = {
    "pedir-moneda": "mostrar en pantalla 'Pedir moneda'",
    "pedir-codigo": "mostrar en pantalla 'Pedir codigo'",
    "servir-c1-esperar": "Mostrar en pantalla 'Sirviendo refresco 1 y esperar'",
    "servir-c2-esperar": "Mostrar en pantalla 'Sirviendo refresco 2 y esperar'",
    "servir-c3-esperar": "Mostrar en pantalla 'Sirviendo refresco 3 y esperar'"
}

# Definir el modelo
#   { Estado, regla, percepcion }: Estado
modelo = {
    ('sin-moneda', 'pedir-moneda', 'moneda'): "recibi-moneda",
    ('recibi-moneda', 'pedir-codigo', 'c1'): "servido-c1",
    ('recibi-moneda', 'pedir-codigo', 'c2'): "servido-c2",
    ('recibi-moneda', 'pedir-codigo', 'c3'): "servido-c3",
    ('servido-c1', 'servir-c1-esperar', 'servido'): "sin-moneda",
    ('servido-c2', 'servir-c2-esperar', 'servido'): "sin-moneda",
    ('servido-c3', 'servir-c3-esperar', 'servido'): "sin-moneda",

    ('recibi-moneda', 'pedir-codigo', 'moneda'): "recibi-moneda"
}


# Función para actualizar el estado
def actualizar_estado(estado, accion, percepcion):
    print("MEDIDAS EN MODELO ", estado, " ", accion, " ", percepcion)
    if (estado, accion, percepcion) in modelo:
        print("SI")
        return modelo[(estado, accion, percepcion)]
    else:
        print("NO")

        return estado


# Inicializar el estado y la acción
estado = 'sin-moneda'
accion = 'pedir-moneda'
accion = reglas[estado]
texto_accion = acciones[accion]
print(texto_accion)
print("Estado: ", estado)


# Ciclo principal del agente
while True:
    print("Ingresar percepción:")
    percepcion = input()

    estado = actualizar_estado(estado, accion, percepcion)
    accion = reglas[estado]
    texto_accion = acciones[accion]

    print(texto_accion)
    print("Estado: ", estado)

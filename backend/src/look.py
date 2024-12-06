def look(arm_position, lrequests, debug=False):
    """
    Implementación del algoritmo LOOK.

    El algoritmo LOOK se mueve en una dirección (hacia la izquierda o derecha),
    atiende las solicitudes en esa dirección, y luego cambia de dirección
    sin necesidad de ir hasta el final del disco.

    Args:
        arm_position (int): Posición inicial del brazo (donde empieza a procesar).
        lrequests (list<int>): Lista de posiciones de las solicitudes.
        debug (bool): Si es True, habilita los mensajes de depuración que muestran el progreso.
    
    Returns:
        dict: Diccionario con:
            - "sequence": Secuencia de las posiciones procesadas.
            - "average": Distancia promedio recorrida por solicitud.
            - "distance": Distancia total recorrida por el brazo.
    """
    distance = 0  # Distancia total recorrida por el brazo
    sequence = []  # Secuencia de posiciones procesadas
    current_pos = arm_position  # Posición inicial del brazo

    # Ordenar las solicitudes para facilitar el recorrido en ambas direcciones
    lrequests = sorted(lrequests)

    # Dividir las solicitudes en dos grupos:
    # - Solicitudes a la derecha (mayores o iguales a la posición actual)
    # - Solicitudes a la izquierda (menores que la posición actual)
    right_requests = [req for req in lrequests if req >= current_pos]
    left_requests = [req for req in lrequests if req < current_pos]

    # **Procesar solicitudes hacia la derecha (en orden creciente)**
    for req in right_requests:
        # Calcular la distancia recorrida hasta la solicitud
        distance += abs(req - current_pos)
        # Actualizar la posición del brazo
        current_pos = req
        # Registrar la posición procesada en la secuencia
        sequence.append(current_pos)
        if debug:
            print("> ", current_pos, "seeked")

    # **Procesar solicitudes hacia la izquierda (en orden decreciente)**
    for req in reversed(left_requests):  # Procesar las solicitudes a la izquierda en orden inverso
        # Calcular la distancia recorrida hasta la solicitud
        distance += abs(req - current_pos)
        # Actualizar la posición del brazo
        current_pos = req
        # Registrar la posición procesada en la secuencia
        sequence.append(current_pos)
        if debug:
            print("> ", current_pos, "seeked")

    # Calcular la distancia promedio recorrida por solicitud
    average = distance / len(lrequests)

    # Retornar los resultados
    return {
        "sequence": sequence,  # Secuencia de posiciones procesadas
        "average": average,    # Distancia promedio recorrida por solicitud
        "distance": distance,  # Distancia total recorrida
    }

# Ejemplo de uso
# print(look(96, [125, 17, 23, 67, 90, 128, 189, 115, 97]))

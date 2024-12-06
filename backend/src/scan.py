def scan(arm_position, lrequests, tracks, debug=False):
    """
    Implementación del algoritmo SCAN (Elevator Algorithm).
    
    El algoritmo SCAN simula el movimiento de un elevador, procesando solicitudes
    en una dirección hasta el final del rango y luego regresando en la dirección opuesta.

    Args:
        arm_position (int): Posición inicial del brazo.
        lrequests (list<int>): Lista de posiciones de las solicitudes.
        tracks (int): Número total de pistas en el disco.
        debug (bool): Si es True, imprime mensajes de depuración sobre el progreso.
    
    Returns:
        dict: Diccionario con:
            - "sequence": Secuencia de pistas procesadas.
            - "average": Distancia promedio recorrida por solicitud.
            - "distance": Distancia total recorrida por el brazo.
    """
    distance = 0  # Distancia total recorrida por el brazo
    sequence = []  # Secuencia en la que se procesan las solicitudes
    current_pos = arm_position  # Posición actual del brazo

    # Agregar las pistas inicial y final del disco a la lista de solicitudes (si no están ya incluidas)
    lrequests = sorted(set(lrequests + [0, tracks - 1]))

    # Dividir las solicitudes en dos grupos:
    # - Solicitudes a la derecha (>= posición actual)
    # - Solicitudes a la izquierda (< posición actual)
    right_requests = [req for req in lrequests if req >= current_pos]
    left_requests = [req for req in lrequests if req < current_pos]

    # **Mover hacia la derecha (creciente)**
    for req in right_requests:
        # Calcular la distancia al siguiente punto
        distance += abs(req - current_pos)
        # Actualizar la posición actual
        current_pos = req
        # Registrar la posición atendida en la secuencia
        sequence.append(current_pos)
        if debug:
            print("> ", current_pos, "seeked")

    # **Mover hacia la izquierda (decreciente)**
    for req in reversed(left_requests):  # Procesar en orden inverso (mayor a menor)
        # Calcular la distancia al siguiente punto
        distance += abs(req - current_pos)
        # Actualizar la posición actual
        current_pos = req
        # Registrar la posición atendida en la secuencia
        sequence.append(current_pos)
        if debug:
            print("> ", current_pos, "seeked")

    # Calcular la distancia promedio recorrida por solicitud
    average = distance / len(lrequests)

    # Retornar los resultados
    return {
        "sequence": sequence,  # Secuencia completa de posiciones atendidas
        "average": average,    # Distancia promedio recorrida por solicitud
        "distance": distance,  # Distancia total recorrida
    }

# Ejemplo de uso
# print(scan(96, [125, 17, 23, 67, 90, 128, 189, 115, 97], 200))

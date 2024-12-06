def clook(arm_position, lrequests, debug=False):
    """
    Implementación del algoritmo C-LOOK (Circular LOOK).

    El algoritmo C-LOOK es una variante del LOOK en la que, al llegar al final de las solicitudes procesadas en una dirección, el brazo regresa al inicio de las solicitudes sin procesar las solicitudes en dirección opuesta. De forma circular, el brazo siempre procesa las solicitudes en la misma dirección.

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

    # Ordenar las solicitudes en orden creciente
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

    # **"Saltar" al inicio de las solicitudes a la izquierda**
    if left_requests:
        # Calcular la distancia para "saltar" al inicio de las solicitudes a la izquierda
        distance += abs(current_pos - left_requests[0])  # Salto circular
        # Mover el brazo a la primera solicitud de la lista de solicitudes a la izquierda
        current_pos = left_requests[0]
        # Registrar el salto al inicio de la lista de solicitudes a la izquierda
        sequence.append(current_pos)
        if debug:
            print("> Jump to ", current_pos)

    # **Procesar solicitudes hacia la derecha desde el inicio de la izquierda**
    for req in left_requests[1:]:
        # Calcular la distancia recorrida hasta la solicitud
        distance += abs(req - current_pos)
        # Actualizar la posición del brazo
        current_pos = req
        # Registrar la posición procesada en la secuencia
        sequence.append(current_pos)
        if debug:
            print("> ", current_pos, "seeked")

    # **Calcular la distancia promedio recorrida por solicitud**
    average = distance / len(lrequests)

    # **Retornar los resultados**
    return {
        "sequence": sequence,  # Secuencia de posiciones procesadas
        "average": average,    # Distancia promedio recorrida por solicitud
        "distance": distance,  # Distancia total recorrida
    }

# Ejemplo de uso
# print(clook(96, [125, 17, 23, 67, 90, 128, 189, 115, 97]))

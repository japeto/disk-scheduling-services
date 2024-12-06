def cscan(arm_position, lrequests, tracks, debug=False):
    """
    Implementación del algoritmo C-SCAN (Circular SCAN).

    El algoritmo C-SCAN es una variante del SCAN en la que, al llegar al final del disco, el brazo regresa al inicio sin procesar las solicitudes de vuelta.
    Esto crea un comportamiento "circular", en el que el brazo siempre se mueve en una sola dirección hasta el final y luego regresa al principio para continuar el procesamiento.

    Args:
        arm_position (int): Posición inicial del brazo (donde empieza a procesar).
        lrequests (list<int>): Lista de posiciones de las solicitudes.
        tracks (int): Número total de pistas del disco.
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

    # Asegurarse de que las pistas inicial (0) y final (tracks-1) estén en la lista de solicitudes
    lrequests = sorted(set(lrequests + [0, tracks - 1]))  # Eliminar duplicados y ordenar las solicitudes

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

    # **Regresar al inicio (salto circular)**
    if right_requests:
        # Calcular la distancia hasta el final del disco (tracks-1)
        distance += abs(tracks - 1 - current_pos)
        # Moverse hasta el final del disco
        current_pos = tracks - 1
        # Registrar el último track en la secuencia
        sequence.append(current_pos)
        
        # Regresar al inicio (posición 0)
        current_pos = 0
        # Registrar el inicio del disco en la secuencia
        sequence.append(current_pos)
        
        if debug:
            print("> ", tracks - 1, "seeked (end)")  # Mostrar la salida hasta el final
            print("> ", current_pos, "seeked (start)")  # Mostrar la llegada al inicio

    # **Procesar solicitudes hacia la derecha desde el inicio**
    for req in left_requests:
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
# print(cscan(96, [125, 17, 23, 67, 90, 128, 189, 115, 97], 200))

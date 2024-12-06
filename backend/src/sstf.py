from heapq import *

def sstf(arm_position, lrequests, debug=False):
    """
    Implementación del algoritmo Shortest Seek Time First (SSTF).
    
    El algoritmo SSTF selecciona la solicitud más cercana a la posición actual del brazo
    para minimizar el tiempo de búsqueda.

    Args:
        arm_position (int): Posición inicial del brazo.
        lrequests (list<int>): Lista de solicitudes de pistas a procesar.
        debug (bool): Si es True, imprime el progreso del algoritmo paso a paso.
    
    Returns:
        dict: Diccionario con:
            - "sequence": Secuencia de pistas procesadas.
            - "average": Distancia promedio recorrida por solicitud.
            - "distance": Distancia total recorrida por el brazo.
    """
    distance = 0  # Distancia total recorrida por el brazo
    n = len(lrequests)  # Número de solicitudes
    current_pos = arm_position  # Posición actual del brazo
    sequence = [current_pos]  # Secuencia en la que se procesan las solicitudes (incluye la posición inicial)
    pending_requests = lrequests.copy()  # Copia de las solicitudes para manipularlas sin afectar la original
    
    # Mientras haya solicitudes pendientes
    while pending_requests:
        # Encontrar la solicitud más cercana a la posición actual del brazo
        closest_request = min(pending_requests, key=lambda req: abs(req - current_pos))
        
        # Calcular la distancia recorrida para llegar a la solicitud más cercana
        distance += abs(closest_request - current_pos)
        
        # Actualizar la posición actual del brazo
        current_pos = closest_request
        
        # Agregar la solicitud atendida a la secuencia
        sequence.append(current_pos)
        
        # Eliminar la solicitud atendida de las pendientes
        pending_requests.remove(closest_request)
        
        # Si está activado el modo de depuración, imprimir el progreso
        if debug:
            print("> ", current_pos, "seeked")
    
    # Calcular la distancia promedio recorrida por solicitud
    average = distance / n
    
    # Retornar los resultados
    return {
        "sequence": sequence,  # Secuencia completa de posiciones atendidas
        "average": average,    # Distancia promedio recorrida por solicitud
        "distance": distance,  # Distancia total recorrida
    }

# Ejemplo de uso
# print(sstf(96, [125, 17, 23, 67, 90, 128, 189, 115, 97]))

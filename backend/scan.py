from heapq import *

def scan(arm_position, lrequests, tracks, debug=False):
    """
    SCAN (Elevator Algorithm) implementation

    Args:
        arm_position (int): Initial arm position
        lrequests (list<int>): List of track requests
        tracks (int): Total number of tracks
        debug (bool): If True, print debug information

    Returns:
        dict: Result with access sequence, total distance, and average
    """
    lrequests = sorted(lrequests)  # Ordena las solicitudes
    below = [req for req in lrequests if req < arm_position]
    above = [req for req in lrequests if req >= arm_position]

    sequence = []  # Para guardar el orden de acceso
    distance = 0

    # Procesar en dirección ascendente
    for req in above:
        distance += abs(req - arm_position)#calcula la distancia
        sequence.append(req)
        arm_position = req

    # Moverse al extremo superior
    if above:
        distance += abs(tracks - 1 - arm_position)
        arm_position = tracks - 1

    # Procesar en dirección descendente
    for req in reversed(below):
        distance += abs(req - arm_position)
        sequence.append(req)
        arm_position = req

    average = distance / len(lrequests)  # Promedio por solicitud

    return {
        "sequence": sequence,
        "distance": distance,
        "average": average,
    }



from heapq import *

def sstf(arm_position, lrequests, debug=False):
    """
    Shortest Seek Time First (SSTF) implementation

    Args:
        arm_position (int): Current arm position
        lrequests (list<int>): List of track requests
    """
    distance = 0
    current_pos = arm_position
    sequence = [arm_position]

    while lrequests: #mientras hayan solicitudes pendientes
        # Encuentra la solicitud más cercana al brazo actual
        nearest = min(lrequests, key=lambda x: abs(x - current_pos))
        distance += abs(nearest - current_pos)#distancia total
        current_pos = nearest
        sequence.append(nearest)
        lrequests.remove(nearest)
        if debug: print("> ", current_pos, "seeked")

    average = distance / len(sequence[1:])  # Excluye la posición inicial
    return {
        "sequence": sequence, #posiciones finales de las solicitudes
        "average": average,
        "distance": distance,
    }

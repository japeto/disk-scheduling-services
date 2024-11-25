from heapq import *

def cscan(arm_position, lrequests, tracks, debug=False):

    distance = 0
    sequence = [arm_position]
    requests = sorted(lrequests + [0, tracks])  # Incluye límites de pista
    
    # Dividir en dos listas
    right = [r for r in requests if r >= arm_position]
    left = [r for r in requests if r < arm_position]

    # Mover hacia la derecha
    for r in right:
        distance += abs(r - arm_position)
        arm_position = r
        sequence.append(r)

    # Regresar al principio
    distance += abs(tracks - arm_position)
    arm_position = 0
    sequence.append(0)

    # Mover a la derecha desde el inicio
    for r in left:
        distance += abs(r - arm_position)
        arm_position = r
        sequence.append(r)

    average = distance / len(lrequests)
    return {
        "sequence": sequence,
        "average": average,
        "distance": distance,
    }

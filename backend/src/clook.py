from heapq import *

def clook(arm_position, lrequests, debug=False):

    distance = 0
    sequence = [arm_position]
    requests = sorted(lrequests)

    # Dividir en dos listas
    right = [r for r in requests if r >= arm_position]
    left = [r for r in requests if r < arm_position]

    # Mover a la derecha
    for r in right:
        distance += abs(r - arm_position)
        arm_position = r
        sequence.append(r)

    # Saltar al inicio de las solicitudes
    arm_position = left[0]
    sequence.append(left[0])

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
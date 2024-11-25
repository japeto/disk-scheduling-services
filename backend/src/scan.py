from heapq import *

def scan(arm_position, lrequests, tracks, debug=False):

    distance = 0
    sequence = [arm_position]
    requests = sorted(lrequests)  # Incluye límites de pista

    # Dividir en dos listas, izquierda y derecha
    left = [r for r in requests if r < arm_position]
    right = [r for r in requests if r >= arm_position]

    # Mover a la derecha primero
    for r in right:
        distance += abs(r - arm_position)
        arm_position = r
        sequence.append(r)
    # Luego mover a la izquierda
    if left :
        distance += tracks - arm_position
        arm_position = tracks

    for r in reversed(left):
        distance += abs(r - arm_position)
        arm_position = r
        sequence.append(r)

    average = distance / len(lrequests)
    return {
        "sequence": sequence,
        "average": average,
        "distance": distance,
    }

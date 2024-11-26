from heapq import *

def look(arm_position, lrequests, debug=False):

    distance = 0
    sequence = [arm_position]
    requests = sorted(lrequests)

    # Dividir en dos listas
    left = [r for r in requests if r < arm_position]
    right = [r for r in requests if r >= arm_position]

    # Mover a la derecha primero
    for r in right:
        distance += abs(r - arm_position)
        arm_position = r
        sequence.append(r)

    # Luego mover a la izquierda
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

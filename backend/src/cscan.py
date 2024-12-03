def cscan(arm_position, requests, tracks, debug=False):
    """
    Circular SCAN (CSCAN) algorithm
    """
    distance = 0
    sequence = []
    requests = sorted(requests)
    right = [r for r in requests if r >= arm_position]
    left = [r for r in requests if r < arm_position]

    # Procesar hacia la derecha
    for r in right:
        distance += abs(arm_position - r)
        sequence.append(r)
        arm_position = r

    # Regresa al inicio del disco
    if left:
        distance += abs(arm_position - 0)
        arm_position = 0
        sequence.append(arm_position)

        # Procesar hacia la derecha desde el principio
        for r in left:
            distance += abs(arm_position - r)
            sequence.append(r)
            arm_position = r

    average = distance / len(requests)
    return {
        "sequence": sequence,
        "distance": distance,
        "average": average,
    }

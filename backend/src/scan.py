def scan(arm_position, requests, tracks, debug=False):
    """
    SCAN algorithm
    """
    distance = 0
    sequence = []
    requests = sorted(requests)
    left = [r for r in requests if r < arm_position]
    right = [r for r in requests if r >= arm_position]

    for r in right:
        distance += abs(arm_position - r)
        sequence.append(r)
        arm_position = r

    for r in reversed(left):
        distance += abs(arm_position - r)
        sequence.append(r)
        arm_position = r

    average = distance / len(requests)
    return {
        "sequence": sequence,
        "distance": distance,
        "average": average,
    }

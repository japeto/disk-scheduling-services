def look(arm_position, lrequests, debug=False):
    distance = 0
    sequence = []
    requests = sorted(lrequests)
    current_pos = arm_position
    # Going in one direction
    for req in requests:
        if req >= current_pos:
            distance += abs(req - current_pos)
            sequence.append(req)
            current_pos = req
    # Reversing direction
    for req in reversed(requests):
        if req < arm_position:
            distance += abs(req - current_pos)
            sequence.append(req)
            current_pos = req
    average = distance / len(lrequests)
    return {
        "sequence": [arm_position] + sequence,
        "average": average,
        "distance": distance,
    }

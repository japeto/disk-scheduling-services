def clook(arm_position, lrequests, debug=False):
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
    # Wrap around to the smallest request
    if requests:
        smallest_request = min(requests)
        distance += abs(current_pos - smallest_request)
        current_pos = smallest_request
        # Process remaining requests
        for req in requests:
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

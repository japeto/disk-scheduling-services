def scan(arm_position, lrequests, tracks, debug=False):
    distance = 0
    sequence = []
    lrequests.extend([0, tracks - 1])
    requests = sorted(lrequests)
    current_pos = arm_position
    # Going in one direction first
    for req in requests:
        if req >= current_pos:
            distance += abs(req - current_pos)
            sequence.append(req)
            current_pos = req
    # Reversing direction
    if current_pos < tracks - 1:
        distance += abs(tracks - 1 - current_pos)
        current_pos = tracks - 1
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

# print(scan(120, [45,133,86,200,42,176,95,140], 250))
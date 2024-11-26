def cscan(arm_position, lrequests, tracks, debug=False):
    distance = 0
    sequence = []
    lrequests.extend([0, tracks - 1])
    requests = sorted(lrequests)
    current_pos = arm_position
    # Going in one direction
    for req in requests:
        if req >= current_pos:
            distance += abs(req - current_pos)
            sequence.append(req)
            current_pos = req
    # Wrap around to the start
    if current_pos != 0:
        distance += abs(tracks - 1 - current_pos) + (tracks - 1)
        current_pos = 0
    # Process the remaining requests
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

print(cscan(140, [10,160,50,90,120,45,80], 180))
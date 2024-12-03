def sstf(arm_position, requests, debug=False):
    """
    Shortest Seek Time First (SSTF)
    """
    distance = 0
    current_pos = arm_position
    sequence = [current_pos]
    requests = requests[:]

    while requests:
        closest_request = min(requests, key=lambda x: abs(x - current_pos))
        distance += abs(closest_request - current_pos)
        current_pos = closest_request
        sequence.append(current_pos)
        requests.remove(closest_request)
        if debug:
            print("> ", current_pos, "processed")

    average = distance / len(sequence)
    return {
        "sequence": sequence,
        "distance": distance,
        "average": average,
    }

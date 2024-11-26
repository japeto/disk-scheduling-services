def look(arm, requests, direction):
    """
    LOOK algorithm.
    Args:
        requests: List of track numbers to service.
        arm: Initial position of the disk arm.
        direction: 'left' or 'right'.

    """
    sequence = []
    distance = 0
    num_requests = len(requests)
    initial_arm = arm
    requests.sort()
    
    if direction == 'left':
        left = [r for r in requests if r <= arm]
        right = [r for r in requests if r > arm]
        for r in reversed(left):
            distance += abs(arm - r)
            arm = r
            sequence.append(r)
        for r in right:
            distance += abs(arm - r)
            arm = r
            sequence.append(r)
    elif direction == 'right':
        left = [r for r in requests if r < arm]
        right = [r for r in requests if r >= arm]
        for r in right:
            distance += abs(arm - r)
            arm = r
            sequence.append(r)
        for r in reversed(left):
            distance += abs(arm - r)
            arm = r
            sequence.append(r)
    
    average = distance / num_requests
    return {
    "sequence": [initial_arm] + sequence,
    "average": average,
    "distance": distance,
    }
def scan(requests, arm, direction, track):
    """
    SCAN algorithm.
    Args:
        requests: List of track numbers to service.
        arm: Initial position of the disk arm.
        direction: 'left' or 'right'.
        track: Maximum track number on the disk.
    """
    sequence = []
    distance = 0
    initial_arm = arm
    num_requests = len(requests)
    requests.sort()
    
    if direction == 'left':
        left = [r for r in requests if r <= arm]
        right = [r for r in requests if r > arm]
        for r in reversed(left):
            distance += abs(arm - r)
            arm = r
            sequence.append(r)
        distance += abs(arm - 0)
        arm = 0
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
        distance += abs(arm - track)
        arm = track
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
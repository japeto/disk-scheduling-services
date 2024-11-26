def clook(arm, requests):
    """
    C-LOOK algorithm.
    Args:
        requests: List of track numbers to service.
        arm: Initial position of the disk arm.
    """
    sequence = []
    distance = 0
    num_requests = len(requests)
    initial_arm = arm
    requests.sort()
    
    right = [r for r in requests if r >= arm]
    left = [r for r in requests if r < arm]
    
    for r in right:
        distance += abs(arm - r)
        arm = r
        sequence.append(r)
    for r in left:
        distance += abs(arm - r)
        arm = r
        sequence.append(r)
    
    average = distance / num_requests
    return {
    "sequence": [initial_arm] + sequence,
    "average": average,
    "distance": distance,
    }
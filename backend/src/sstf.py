def sstf(arm, requests):
    """
    Shortest Seek Time First algorithm.
    requests: List of track numbers to service.
    arm: Initial position of the disk arm.
    """
    sequence = []
    distance = 0
    initial_arm = arm
    num_requests = len(requests)
    while requests:
        distances = [(abs(arm - req), req) for req in requests]
        closest = min(distances, key=lambda x: x[0])
        distance += closest[0]
        arm = closest[1]
        sequence.append(arm)
        requests.remove(arm)
    
    average = distance / num_requests
    return {
    "sequence": [initial_arm] + sequence,
    "average": average,
    "distance": distance,
    }

def cscan(arm, requests, track):
    """
    C-SCAN algorithm.
    Args:
        requests: List of track numbers to service.
        arm: Initial position of the disk arm.
        track: Maximum track number on the disk.
    """
    sequence = []
    distance = 0
    rTrack = track - 1 
    num_requests = len(requests)
    initial_arm = arm
    requests.sort()
    
    right = [r for r in requests if r >= arm]
    left = [r for r in requests if r < arm]
    
    for r in right:
        distance += abs(arm - r)
        print(distance)
        arm = r
        sequence.append(r)
    
    if left:
        
        if arm == rTrack:
          arm = 0 
          sequence.append(arm)
          distance += abs(track - arm - 1)

        else: 
          distance += abs(arm - track + 1)
          print(distance)
          sequence.append(track - 1) 
          arm = 0
          sequence.append(arm)
          distance += abs(track - arm - 1)

        for r in left:
            distance += abs(arm - r)
            print(distance)
            arm = r
            sequence.append(r)
    
    average = distance / num_requests
    return {
    "sequence": [initial_arm] + sequence,
    "average": average,
    "distance": distance,
    }


#print(cscan(50, [82,170,43,140,24,16,190],200))
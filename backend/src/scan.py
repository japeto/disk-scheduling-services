#scan.py
def scan(arm_position, lrequests, total_tracks):
    lrequests.sort()
    left = [r for r in lrequests if r < arm_position]
    right = [r for r in lrequests if r >= arm_position]
    
    left.reverse()
    
    # Traverse left first
    distance = 0
    current_pos = arm_position
    for request in left:
        distance += abs(request - current_pos)
        current_pos = request
    
    # Then traverse right
    for request in right:
        distance += abs(request - current_pos)
        current_pos = request
    
    average = distance / len(lrequests)
    return {
        "sequence": [arm_position] + left + right,
        "average": average,
        "distance": distance
    }

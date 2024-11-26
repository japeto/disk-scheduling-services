# clook.py
def clook(arm_position, lrequests):
    lrequests.sort()
    right = [r for r in lrequests if r >= arm_position]
    left = [r for r in lrequests if r < arm_position]
    
    # Traverse right first
    distance = 0
    current_pos = arm_position
    for request in right:
        distance += abs(request - current_pos)
        current_pos = request
    
    # Then wrap around and go to the beginning
    for request in left:
        distance += abs(request - current_pos)
        current_pos = request
    
    average = distance / len(lrequests)
    return {
        "sequence": [arm_position] + right + left,
        "average": average,
        "distance": distance
    }

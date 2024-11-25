# sstf.py
def sstf(arm_position, lrequests):
    requests = sorted(lrequests, key=lambda x: abs(x - arm_position))
    distance = 0
    current_pos = arm_position
    for request in requests:
        distance += abs(request - current_pos)
        current_pos = request
    
    average = distance / len(lrequests)
    return {
        "sequence": [arm_position] + requests,
        "average": average,
        "distance": distance
    }

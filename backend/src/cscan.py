
from heapq import *

def cscan(arm_position, lrequests, tracks, debug=False):

    # order the requests
    requests.sort()

    # split the requests into two groups based on the arm position
    left_requests = [r for r in requests if r < arm_position]
    right_requests = [r for r in requests if r >= arm_position]

    # move to right
    distance = 0
    current_position =arm_position 
    sequence = [arm_position]

    # get the distance to the right
    for request in right_requests:
        distance += abs(request - current_position)
        current_position = request
        sequence.append(request)

    # move to the end of the disk
    distance += abs(tracks - 1 - current_position)
    current_position = 0

    # move to the left 
    for request in left_requests:
        distance += abs(request - current_position)
        current_position = request
        sequence.append(request)


    return {
        "sequence": sequence,
        "average": distance / len(requests),
        "distance": distance
    }


from heapq import *




def scan(arm_position, lrequests, tracks, debug=False):
    """
    SCAN Disk Scheduling Algorithm
    Args:
        arm_position (int): initial position of the arm
        lrequests (list<int>): list of track requests
        tracks (int): total number of tracks (cylinders)
        debug (bool): if True, print debug information
    """
    # Validar entradas
    if not isinstance(lrequests, list) or len(lrequests) == 0:
        raise ValueError("The request list must be a non-empty list of integers.")
    if not all(isinstance(x, int) for x in lrequests):
        raise ValueError("All elements in the request list must be integers.")
    if not isinstance(arm_position, int):
        raise ValueError("The arm position must be an integer.")

    # an item greater than the total number of tracks

    if not all(x < tracks for x in lrequests):
        raise ValueError("All requests must be less than the total number of tracks.")


    
    distance = 0
    n = len(lrequests)
    lrequests_copy = lrequests.copy()

    # split the requests into two groups based on the arm position
    left = [x for x in lrequests_copy if x < arm_position]
    right = [x for x in lrequests_copy if x >= arm_position]


    # sort the requests
    left.sort(reverse=True)  # orders the requests from largest to smallest
    right.sort()  # orders the requests from smallest to largest 

    # move to right 
    total_distance = 0
    sequence = [arm_position]
    for track in right:
        total_distance += abs(track - arm_position)
        arm_position = track
        sequence.append(track)

    # move to left 
    for track in left:
        total_distance += abs(track - arm_position)
        arm_position = track
        sequence.append(track)

    average = total_distance / n
    return {
        "sequence": sequence,
        "average": average,
        "distance": total_distance
    }


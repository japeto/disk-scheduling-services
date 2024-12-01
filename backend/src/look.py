from heapq import *

def look(arm_position, lrequests, tracks, debug=False):
    """
    SCAN (Elevator Algorithm) implementation with disk size consideration.

    Args:
        arm_position (int): arm position
        lrequests (list<int>): request list
        tracks (int): Total number of tracks in the disk.

    Returns:
        dict: Contains the sequence of accesses, total distance, and average distance.
    """

    lrequests = sorted(lrequests)

    below = [req for req in lrequests if req < arm_position]
    above = [req for req in lrequests if req >= arm_position]

    sequence = above

    if below:
        sequence += below[::-1]

    distance = 0
    current_pos = arm_position
    for a_request in sequence:
        distance += abs(a_request - current_pos)
        current_pos = a_request
        if debug:
            print("> ", current_pos, "seeked")

    average = distance / len(lrequests)

    return {
        "sequence": [arm_position] + sequence,
        "average": average,
        "distance": distance,
    }

# print(look(96, [125,17,23,67,90,128,189,115,97], 200))
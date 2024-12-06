
from heapq import *


def sstf(arm_position, lrequests, debug=False):

    """
    Shortest Seek Time First (SSTF) algorithm
    
    Args:
        arm_position (int): initial arm position
        lrequests (list<int>): list of track requests
        debug (bool): if True, print debug information

    Returns:
        dict: containing the sequence of tracks, total distance, and average distance
    """    
    distance = 0
    n = len(lrequests)
    current_pos = arm_position
    lrequests_copy = lrequests.copy()
    sequence = [arm_position]

    print(lrequests)

    while len(lrequests_copy) > 0:
        # calculate the distance between the current position and all requests
        request_distances = list(map(lambda x: abs(x - current_pos), lrequests_copy))
        
        if debug: print("Request distances:", request_distances)

        # find the minimum distance 
        min_distance = min(request_distances)
        min_distance_index = request_distances.index(min_distance)

        # move the arm to the closest request
        distance += min_distance
        current_pos = lrequests_copy.pop(min_distance_index)
        sequence.append(current_pos)

        if debug: print("> ", current_pos, "seeked")

    average = distance / n

    return {
        "sequence": sequence,
        "average": average,
        "distance": distance,
    }

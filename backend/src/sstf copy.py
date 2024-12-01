from heapq import *

def sstf(arm_position, lrequests, debug=False):
    """
    Shortest Seek Time First implementation.

    Args:
        arm_position (int): arm position
        lrequests (list<int>): request list
        debug (bool): if True, prints the movement details.
    """
    distance = 0
    n = len(lrequests)
    current_pos = arm_position
    lrequests = lrequests[:]
    sequence = [arm_position]

    for i in range(n):

        closest_request = min(lrequests, key=lambda x: (abs(x - current_pos), -x))

        distance += abs(closest_request - current_pos)
        current_pos = closest_request

        sequence.append(current_pos)
        lrequests.remove(closest_request)
    

    average = distance / n
    return {
        "sequence": sequence,
        "average": average,
        "distance": distance,
    }

print(sstf(96, [125,17,23,67,90,128,189,115,97]))
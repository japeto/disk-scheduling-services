from heapq import *

def sstf(arm_position, lrequests, debug=False):
    """
    Shortest Seek Time First implementation

    Args:
        arm_position (int): arm position
        lrequests (list<int>): request list
    """
    distance = 0
    current_pos = arm_position
    sequence = [arm_position]
    requests = lrequests[:]

    while requests:
        closest_request = min(requests, key=lambda x: abs(x - current_pos))
        distance += abs(closest_request - current_pos)
        current_pos = closest_request
        sequence.append(current_pos)
        requests.remove(closest_request)
        if debug: print("> ", current_pos, "seeked")

    average = distance / len(lrequests)
    return {
        "sequence": sequence,
        "average": average,
        "distance": distance,
    }

# print(sstf(96, [125,17,23,67,90,128,189,115,97]))

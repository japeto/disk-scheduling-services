from heapq import *

def sstf(arm_position, lrequests, debug=False):

    distance = 0
    sequence = [arm_position]
    requests = lrequests[:]
    
    while requests:
        # Encuentra la solicitud más cercana
        closest_request = min(requests, key=lambda r: abs(r - arm_position))
        distance += abs(closest_request - arm_position)
        arm_position = closest_request
        sequence.append(closest_request)
        requests.remove(closest_request)
        if debug:
            print("> ", arm_position, "seeked")
    
    average = distance / len(lrequests)
    return {
        "sequence": sequence,
        "average": average,
        "distance": distance,
    }


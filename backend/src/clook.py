def clook(tracks, arm_position, lrequests, debug=False):
    """
    C-LOOK Disk Scheduling Algorithm

    Args:
        tracks (int) : number of cylinders
        arm_position (int): arm position
        lrequests (list<int>): request list
    """
    distance = 0
    n = len(lrequests)
    current_pos = arm_position

    olders = []
    minors = []
    ignored = 0

    for x in lrequests:
        if x >= 0 and x <= tracks:
            if x >= arm_position:
                olders.append(x)
            else:
                minors.append(x)
        else:
            ignored += 1

    olders.sort()
    minors.sort()

    request = olders + minors
    print(request)

    for a_request in request:
        distance += abs(a_request - current_pos)
        current_pos = a_request
        if debug:
            print("> ", current_pos, "seeked")
    
    average = distance / (n - ignored)

    return {
        "sequence": [arm_position] + request,
        "average": average,
        "distance": distance
        }

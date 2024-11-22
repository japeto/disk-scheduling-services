def look(tracks, arm_position, lrequests, debug= False):
    """
    Improved version of the Elevator Algorithm

    Args:
        tracks (int) : number of cylinders
        arm_position (int): arm position
        lrequests (list<int>): request list
    """
    distance=0
    n = len(lrequests)
    current_pos = arm_position

    olders = []
    minors = []
    ignored = []
    
    for x in lrequests:
        if x >= 0 and x <= tracks:
            if x > arm_position:
                olders.append(x)
            else:
                minors.append(x)
        else:
            ignored.append(x)

    olders.sort()
    minors.sort(reverse=True)

    request = olders + minors

    for a_request in request:
        distance += abs(a_request-current_pos)
        current_pos=a_request
        if debug: print("> ", current_pos ,"seeked")
    
    average = distance / (n - len(ignored)) 

    return {
        "sequence": [arm_position] + request,
        "average": average,
        "distance": distance,
        "ignored": ignored
    }
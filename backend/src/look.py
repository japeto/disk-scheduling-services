



def look(arm_position, lrequests, tracks, debug=False):
    """
    LOOK Disk Scheduling Algorithm
    
    Args:
        arm_position (int): The initial arm position on the disk.
        lrequests (list): A list of requested tracks.
        tracks (int): The total number of tracks available.
        debug (bool): If set to True, debug information will be printed.
        
    Returns:
        dict: A dictionary containing the sequence of requests, the total distance traveled, and the average distance per request.
    """

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


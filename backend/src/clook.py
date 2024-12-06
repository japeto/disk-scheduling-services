
def clook(arm_position, lrequests, tracks):
    """
    CLOOK Disk Scheduling Algorithm

    Args:
        arm_position (int): The initial arm position on the disk.
        lrequests (list): A list of requested tracks.
        tracks (int): Total number of tracks on the disk.

    Returns:
        dict: A dictionary containing the sequence of requests, the total distance traveled, and the average distance per request.
    """
    
    # Validate the inputs
    if not all(x < tracks for x in lrequests):
        raise ValueError("All requests must be less than the total number of tracks.")
    
    # Initialize variables
    distance = 0
    current_pos = arm_position
    lrequests_copy = sorted(lrequests)  # Sort the requests in ascending order
    
    # Split the requests into two lists: less than and greater than current_pos
    left = [req for req in lrequests_copy if req < current_pos]
    right = [req for req in lrequests_copy if req > current_pos]
    
    # Initialize the seek sequence
    seek_sequence = []
    
    # Traverse in the direction of the closest side first
    if current_pos in lrequests_copy:
        seek_sequence.append(current_pos)
    
    # Process requests to the right first
    if right:
        seek_sequence += right
        distance += abs(current_pos - right[0])
        current_pos = right[-1]
    
    # After reaching the end, the arm jumps to the lowest position and continues to process remaining requests
    if left:
        distance += abs(current_pos - left[0])  # Jump back to the start of the left
        current_pos = left[0]
        seek_sequence += left

    # Calculate the average distance
    average = distance / len(lrequests) if len(lrequests) > 0 else 0

    # Return the result
    return {
        "sequence": seek_sequence,
        "average": average,
        "distance": distance,
    }

def sstf(arm_position, lrequests, debug=False):
    """
    Shortest Seek Time First (SSTF) implementation

    Args:
        arm_position (int): Initial arm position.
        lrequests (list<int>): Request list.
        debug (bool): If True, prints step-by-step movements.
    """
    distance = 0
    current_pos = arm_position
    sequence = [current_pos]  # Track the sequence of movements

    while lrequests:
        # Find the request with the shortest seek time
        nearest_request = min(lrequests, key=lambda x: abs(x - current_pos))
        seek_distance = abs(nearest_request - current_pos)
        distance += seek_distance

        if debug:
            print(f"> Moving from {current_pos} to {nearest_request} (distance: {seek_distance})")

        # Update the current position and sequence
        current_pos = nearest_request
        sequence.append(current_pos)

        # Remove the processed request
        lrequests.remove(nearest_request)

    average = distance / len(sequence[1:])  # Exclude the initial position from count
    return {
        "sequence": sequence,
        "average": average,
        "distance": distance,
    }

# Example usage:
# print(sstf(96, [125, 17, 23, 67, 90, 128, 189, 115, 97], debug=True))

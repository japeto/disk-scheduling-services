def sstf(arm_position, lrequests, debug=False):
    
    total_distance = 0  # Initialize total distance traveled
    current_position = arm_position  # Start at the arm's initial position
    access_sequence = [current_position]  # List to track the sequence of movements

    while lrequests:
        # Find the request with the shortest seek time (min distance)
        closest_request = min(lrequests, key=lambda x: abs(x - current_position))
        seek_distance = abs(closest_request - current_position)
        total_distance += seek_distance  # Add to total distance

        if debug:
            print(f"> Moving from {current_position} to {closest_request} (distance: {seek_distance})")

        # Update the current position and append to the sequence
        current_position = closest_request
        access_sequence.append(current_position)

        # Remove the processed request from the list
        lrequests.remove(closest_request)

    # Calculate the average distance, excluding the starting position
    avg_distance = round(total_distance / len(access_sequence[1:]), 2)  # Exclude initial position

    return {
        "sequence": access_sequence,  # Full sequence of movements
        "average": avg_distance,  # Average seek time, rounded
        "distance": round(total_distance, 2),  # Total distance, rounded
    }

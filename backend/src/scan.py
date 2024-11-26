def scan(arm_position, lrequests, tracks, debug=False):
    # Initialize total distance and sequence of requests
    total_distance = 0  
    access_sequence = []  
    
    # Add endpoints to the list of requests
    lrequests.extend([0, tracks - 1])  
    sorted_requests = sorted(lrequests)  # Sort the requests
    current_position = arm_position  
    
    # Process requests moving forward
    for request in sorted_requests:
        if request >= current_position:
            total_distance += abs(request - current_position)  # Calculate distance
            access_sequence.append(request)  # Append request to sequence
            current_position = request  # Update current position
    
    # Handle the reverse direction
    if current_position < tracks - 1:
        total_distance += abs((tracks - 1) - current_position)  # Distance to the last track
        current_position = tracks - 1  # Update to the last track
    
    # Process remaining requests in reverse
    for request in reversed(sorted_requests):
        if request < arm_position:
            total_distance += abs(request - current_position)  # Calculate distance
            access_sequence.append(request)  # Append request to sequence
            current_position = request  # Update current position
    
    # Compute the average distance and round to two decimal places
    avg_distance = round(total_distance / len(lrequests), 2)  
    
    # Return the results
    return {
        "sequence": [arm_position] + access_sequence,  # Full sequence of accesses
        "average": avg_distance,  # Rounded average distance
        "distance": round(total_distance, 2),  # Total distance traveled, rounded
    }

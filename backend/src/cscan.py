def cscan(arm_position, lrequests, tracks, debug=False):
    # Initialize total distance and sequence of requests
    total_distance = 0  
    access_sequence = []  
    
    # Add endpoints to the request list
    lrequests.extend([0, tracks - 1])  
    sorted_requests = sorted(lrequests)  # Sort the requests
    current_position = arm_position  
    
    # Process requests moving forward
    for request in sorted_requests:
        if request >= current_position:
            total_distance += abs(request - current_position)  # Calculate distance to next request
            access_sequence.append(request)  # Add to the sequence
            current_position = request  # Update current position
    
    # Handle the wrap-around to the start of the disk
    if current_position != 0:
        total_distance += abs((tracks - 1) - current_position) + (tracks - 1)  # Wrap-around distance
        current_position = 0  # Reset position to the start
    
    # Process remaining requests in reverse
    for request in sorted_requests:
        if request < arm_position:
            total_distance += abs(request - current_position)  # Calculate distance
            access_sequence.append(request)  # Add to the sequence
            current_position = request  # Update position
    
    # Compute the average distance and round to two decimal places
    avg_distance = round(total_distance / len(lrequests), 2)  
    
    # Return the results
    return {
        "sequence": [arm_position] + access_sequence,  # Full sequence of accessed positions
        "average": avg_distance,  # Rounded average distance
        "distance": round(total_distance, 2),  # Total distance traveled, rounded
    }

def look(arm_position, lrequests, debug=False):
    # Initialize total distance and sequence of accesses
    total_distance = 0  
    access_sequence = []  
    
    # Sort the list of requests in ascending order
    sorted_requests = sorted(lrequests)  
    current_position = arm_position  
    
    # Process requests in the forward direction
    for request in sorted_requests:
        if request >= current_position:
            total_distance += abs(request - current_position)  # Add distance to next request
            access_sequence.append(request)  # Append request to sequence
            current_position = request  # Update current position
    
    # Process requests in the reverse direction
    for request in reversed(sorted_requests):
        if request < arm_position:
            total_distance += abs(request - current_position)  # Add distance to next request
            access_sequence.append(request)  # Append request to sequence
            current_position = request  # Update current position
    
    # Compute the average distance and round to two decimal places
    avg_distance = round(total_distance / len(lrequests), 2)  
    
    # Return the results
    return {
        "sequence": [arm_position] + access_sequence,  # Full sequence of requests processed
        "average": avg_distance,  # Rounded average distance
        "distance": round(total_distance, 2),  # Total distance traveled, rounded
    }

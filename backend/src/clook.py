def clook(arm_position, lrequests, debug=False):
    # Initialize the total distance traveled and the sequence of accesses
    total_distance = 0  
    access_sequence = []  
    # Sort the list of requests
    sorted_requests = sorted(lrequests)  
    current_position = arm_position  
    
    # Process requests in the forward direction
    for request in sorted_requests:
        if request >= current_position:
            total_distance += abs(request - current_position)  # Calculate distance to next request
            access_sequence.append(request)  # Add to the access sequence
            current_position = request  # Update current position
    
    # Wrap around to the smallest request if needed
    if sorted_requests:
        smallest_request = min(sorted_requests)  # Find the smallest request
        total_distance += abs(current_position - smallest_request)  # Add wrap-around distance
        current_position = smallest_request  # Update position to smallest request
        
        # Process remaining requests in the reverse direction
        for request in sorted_requests:
            if request < arm_position:
                total_distance += abs(request - current_position)  # Calculate distance
                access_sequence.append(request)  # Add to the access sequence
                current_position = request  # Update current position
    
    # Compute the average distance and round to two decimal places
    avg_distance = round(total_distance / len(lrequests), 2)  
    
    # Return the results
    return {
        "sequence": [arm_position] + access_sequence,  # Full sequence of positions
        "average": avg_distance,  # Rounded average distance
        "distance": round(total_distance, 2),  # Total distance, rounded
    }


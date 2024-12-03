def clook (arm_position, lrequests, debug = False):
	"""
	CLOOK disk scheduling algorithm

	Args:
		arm_position (int): arm position
		lrequests (list<int>): request list
	"""

	distance = 0
	n = len(lrequests)
	current_pos = arm_position
	lrequests.sort()

	left = [req for req in lrequests if req < arm_position]
	right = [req for req in lrequests if req >= arm_position]

	sequence = [current_pos]
	for direction in [right, left]:
		for request in direction:
			distance += abs(request - current_pos)
			current_pos = request
			sequence.append(current_pos)
	average = distance / n
	return { "sequence": sequence, "average": average, "distance": distance }

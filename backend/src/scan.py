def scan(tracks, arm_position, lrequests, debug=False):
  """
  Elevator Algorithm

  Args:
      tracks (int) : number of cylinders
      arm_position (int): arm position
      lrequests (list<int>): request list
  """

  distance=0
  n = len([x for x in lrequests if 0 < x < tracks])
  current_pos = arm_position

  olders = [x for x in lrequests if x > arm_position and x < tracks]
  olders.sort()

  minors = [x for x in lrequests if x < arm_position and x > 0]
  minors.sort(reverse=True)

  request = olders + [tracks] + minors

  sequence = [current_pos]

  for a_request in request:
    distance += abs(a_request-current_pos)
    current_pos=a_request
    sequence.append(current_pos)
    if debug: print("> ", current_pos ,"seeked")
  
  average = distance / n

  return {
    "sequence": sequence,
    "average": average,
    "distance": distance,
  }
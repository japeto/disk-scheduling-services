def sstf(arm_position, lrequests, debug=False):
  """
  Shortest Seek Time First

  Args:
      arm_position (int): arm position
      lrequests (list<int>): request list
  """

  distance=0
  n=len(lrequests)
  current_pos=arm_position

  lrequests.sort(reverse=True)

  request = []

  for i in range(n):
    if (i == 0):
      smallest_difference = min(lrequests, key=lambda x: abs(x - arm_position))
    else:
      smallest_difference = min(lrequests, key=lambda x: abs(x - request[-1]))

    request.append(smallest_difference)
    lrequests.remove(smallest_difference)

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
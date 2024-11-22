def sstf(arm_position, lrequests, debug=False):
  """
  First Come First Serve implementation

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
      menor_diferencia = min(lrequests, key=lambda x: abs(x - arm_position))
    else:
      menor_diferencia = min(lrequests, key=lambda x: abs(x - request[-1]))

    request.append(menor_diferencia)
    lrequests.remove(menor_diferencia)

  for a_request in request:
    distance += abs(a_request-current_pos)
    current_pos=a_request
    if debug: print("> ", current_pos ,"seeked")
  
  average = distance / n
  return {
    "sequence": [arm_position] + request,
    "average": average,
    "distance": distance,
  }
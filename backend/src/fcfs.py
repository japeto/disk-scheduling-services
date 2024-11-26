from heapq import *

def fcfs(arm_position, lrequests, debug=False):
  """
  First Come First Serve implementation

  Args:
      arm_position (int): arm position
      lrequests (list<int>): request list
  """
  distance=0
  n=len(lrequests)
  current_pos=arm_position
  for a_request in lrequests:
    distance += abs(a_request-current_pos)
    current_pos=a_request
    if debug: print("> ", current_pos ,"seeked")
  
  average=distance / n
  return {
    "sequence": [arm_position] + lrequests,
    "average": average,
    "distance": distance,
  }

#print(fcfs(96, [125,17,23,67,90,128,189,115,97]))

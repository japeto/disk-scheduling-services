from heapq import *

def fcfs(arm_position, lrequests, debug=False):

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
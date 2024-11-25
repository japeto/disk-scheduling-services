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

# print(fcfs(96, [125,17,23,67,90,128,189,115,97]))

def sstf(arm_position, lrequests, debug=False):
    """
    Shortest Seek Time First implementation

    Este algoritmo selecciona la solicitud más cercana a
    la posición actual del brazo del disco.

    Args:
        arm_position (int): arm position
        lrequests (list<int>): request list

    """
    distance = 0
    sequence = [arm_position]
    current_pos = arm_position
    requests = lrequests.copy()

    while requests:
      closest = min(requests, key=lambda x: abs(x - current_pos))
      distance += abs(closest - current_pos)
      current_pos = closest
      sequence.append(current_pos)
      requests.remove(closest)
      if debug: print("> ", current_pos, "seeked")

    average = distance / len(lrequests)
    return {
      "sequence": sequence,
      "average": average,
      "distance": distance,
    }


def scan(arm_position, lrequests, tracks, debug=False):
  """
  SCAN implementation

  En el algoritmo SCAN, el brazo del disco se mueve en una
  dirección hasta llegar al final, y luego invierte la
  dirección y mueve el brazo en la dirección opuesta,
  atendiendo las solicitudes en ese orden.

  Args:
      arm_position (int): arm position
      lrequests (list<int>): request list
      tracks (int): number of cylinders
  """
  distance = 0
  sequence = [arm_position]
  current_pos = arm_position
  requests = sorted(lrequests)

  left = [req for req in requests if req < current_pos]
  right = [req for req in requests if req >= current_pos]

  for direction in [right, left[::-1]]:
    for req in direction:
      distance += abs(req - current_pos)
      current_pos = req
      sequence.append(req)
      if debug: print("> ", current_pos, "seeked")

  average = distance / len(lrequests)
  return {
    "sequence": sequence,
    "average": average,
    "distance": distance,
  }


def cscan(arm_position, lrequests, tracks, debug=False):
    """
    Circular SCAN implementation

    El algoritmo C-SCAN es una versión modificada de SCAN
    donde el brazo del disco, al llegar al final, regresa
    al inicio y continúa atendiendo solicitudes.


    Args:
        arm_position (int): arm position
        lrequests (list<int>): request list
        tracks (int): number of cylinders
    """
    distance = 0
    sequence = [arm_position]
    current_pos = arm_position
    requests = sorted(lrequests)

    # Split requests into those to the right and left of the arm position
    right = [req for req in requests if req >= current_pos]
    left = [req for req in requests if req < current_pos]

    # Service requests on the right, then jump to the start
    for req in right:
      distance += abs(req - current_pos)
      current_pos = req
      sequence.append(req)
      if debug: print("> ", current_pos, "seeked")

    # Jump to the start (tracks = 0) and service requests on the left
    if right:
      distance += abs(tracks - 1 - current_pos)  # Move to the end of the disk
      current_pos = 0
      sequence.append(0)
      if debug: print("> Jump to 0")

    for req in left:
      distance += abs(req - current_pos)
      current_pos = req
      sequence.append(req)
      if debug: print("> ", current_pos, "seeked")

    average = distance / len(lrequests)
    return {
      "sequence": sequence,
      "average": average,
      "distance": distance,
    }


def look(arm_position, lrequests, debug=False):
  """
  LOOK implementation

  El algoritmo LOOK es similar a SCAN, pero no va hasta el
  final del disco. En lugar de eso, el brazo se mueve solo
  hasta el último cilindro que tiene una solicitud.

  Args:
      arm_position (int): arm position
      lrequests (list<int>): request list
  """
  distance = 0
  sequence = [arm_position]
  current_pos = arm_position
  requests = sorted(lrequests)

  # Split requests into those to the right and left of the arm position
  left = [req for req in requests if req < current_pos]
  right = [req for req in requests if req >= current_pos]

  # Service requests to the right first, then to the left
  for direction in [right, left[::-1]]:
    for req in direction:
      distance += abs(req - current_pos)
      current_pos = req
      sequence.append(req)
      if debug: print("> ", current_pos, "seeked")

  average = distance / len(lrequests)
  return {
    "sequence": sequence,
    "average": average,
    "distance": distance,
  }

def clook(arm_position, lrequests, debug=False):
    """
    Circular LOOK implementation

    C-LOOK es una versión modificada del LOOK. Cuando llega
    al último cilindro en la dirección de movimiento,
    regresa al primer cilindro con una solicitud.


    Args:
        arm_position (int): arm position
        lrequests (list<int>): request list
    """
    distance = 0
    sequence = [arm_position]
    current_pos = arm_position
    requests = sorted(lrequests)

    # Split requests into those to the right and left of the arm position
    right = [req for req in requests if req >= current_pos]
    left = [req for req in requests if req < current_pos]

    # Service requests on the right, then jump to the lowest request
    for req in right:
      distance += abs(req - current_pos)
      current_pos = req
      sequence.append(req)
      if debug: print("> ", current_pos, "seeked")

    # Jump to the smallest request and continue
    if right and left:
      distance += abs(current_pos - left[0])
      current_pos = left[0]
      sequence.append(current_pos)
      if debug: print("> Jump to ", current_pos)

    for req in left:
      distance += abs(req - current_pos)
      current_pos = req
      sequence.append(req)
      if debug: print("> ", current_pos, "seeked")

    average = distance / len(lrequests)
    return {
      "sequence": sequence,
      "average": average,
      "distance": distance,
    }









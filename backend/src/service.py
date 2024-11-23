from flask import Flask, request, jsonify

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from fcfs import fcfs

@app.route("/", methods=['GET'])
def hello():
  return {
    "message": "use /usage to get information"
  }
  
@app.route("/usage", methods=['GET'])
def help():
  return {
    "message": "use FIFO, SSTF, SCAN or CSCAN algorithms",
    "instructions":{
      "endpoint":"/sched",
      "method": "POST",
      "payload":{
        "algorithm": "1:FCFS, 2:SSTF, 3:SCAN, 4:CSCAN, 5:LOOK, 6:CLOOK",
        "tracks": "number of cylinders",
        "arm": "initial position",
        "requests":"list of tracks"
      },
      "payload_example":{
        "algorithm": 1,
        "tracks":200,
        "arm": 96,
        "requests":[125,17,23,67,90,128,189,115,97]
      },
      "description": "This endpoint perform disk scheduling algorithms"
    }
  }
  
@app.route("/sched", methods=['POST'])
def sched():
  data = request.get_json()
  algorithm = data.get("algorithm")
  tracks = data.get("tracks")
  arm = data.get("arm")
  requests = data.get("requests")
  
  if algorithm == 1:  ## FCFS
    result = fcfs(arm, requests)
  else:
    return jsonify({"error": "Invalid algorithm"}), 400
  
  return jsonify({
    "result": result
  }), 200
    
  
  

  
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000)


"""

# Algoritmos

def sstf(request_data):
    requests = sorted(request_data.get('requests', []))
    head_position = request_data.get('head_position', 0)
    seek_order = []
    while requests:
        closest_request = min(requests, key=lambda x: abs(x - head_position))
        seek_order.append(closest_request)
        head_position = closest_request
        requests.remove(closest_request)
    return {"order": seek_order}

def scan(request_data):
    requests = sorted(request_data.get('requests', []))
    head_position = request_data.get('head_position', 0)
    direction = request_data.get('direction', 'left')
    if direction == 'left':
        requests = [0] + requests[::-1]
    else:
        requests = requests + [100]
    seek_order = []
    for request in requests:
        if (direction == 'left' and request <= head_position) or (direction == 'right' and request >= head_position):
            seek_order.append(request)
    return {"order": seek_order}

def cscan(request_data):
    requests = sorted(request_data.get('requests', []))
    head_position = request_data.get('head_position', 0)
    seek_order = [head_position]
    right = [r for r in requests if r > head_position]
    left = [r for r in requests if r < head_position]
    seek_order.extend(right)
    seek_order.append(max(requests))
    seek_order.extend(left)
    return {"order": seek_order}

def look(request_data):
    requests = sorted(request_data.get('requests', []))
    head_position = request_data.get('head_position', 0)
    direction = request_data.get('direction', 'left')
    if direction == 'left':
        requests = [0] + requests[::-1]
    else:
        requests = requests + [100]
    seek_order = []
    for request in requests:
        if (direction == 'left' and request <= head_position) or (direction == 'right' and request >= head_position):
            seek_order.append(request)
    return {"order": seek_order}

def clook(request_data):
    requests = sorted(request_data.get('requests', []))
    head_position = request_data.get('head_position', 0)
    right = [r for r in requests if r > head_position]
    left = [r for r in requests if r < head_position]
    seek_order = [head_position]
    seek_order.extend(right)
    seek_order.extend(left)
    return {"order": seek_order}

# Endpoints

@app.route('/sstf', methods=['POST'])
def sstf_endpoint():
    data = request.get_json()
    result = sstf(data)
    return jsonify(result)

@app.route('/scan', methods=['POST'])
def scan_endpoint():
    data = request.get_json()
    result = scan(data)
    return jsonify(result)

@app.route('/cscan', methods=['POST'])
def cscan_endpoint():
    data = request.get_json()
    result = cscan(data)
    return jsonify(result)

@app.route('/look', methods=['POST'])
def look_endpoint():
    data = request.get_json()
    result = look(data)
    return jsonify(result)

@app.route('/clook', methods=['POST'])
def clook_endpoint():
    data = request.get_json()
    result = clook(data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
"""
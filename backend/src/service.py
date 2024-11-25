from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import json

# Importamos los algoritmos
from fcfs import fcfs
from sstf import sstf
from scan import scan
from cscan import cscan
from look import look
from clook import clook

app = Flask(__name__)
CORS(app)

# Ruta base de la carpeta `inputs`
BASE_DIR = os.getcwd()
INPUTS_FOLDER = os.path.join(BASE_DIR, 'inputs')

@app.route("/", methods=['GET'])
def hello():
    return {
        "message": "Use /usage to get information about the API"
    }
  
@app.route("/usage", methods=['GET'])
def help():
    return {
        "message": "Use FIFO, SSTF, SCAN, CSCAN, LOOK or CLOOK algorithms",
        "instructions": {
            "endpoint": "/sched",
            "method": "POST",
            "payload": {
                "algorithm": "1:FCFS, 2:SSTF, 3:SCAN, 4:CSCAN, 5:LOOK, 6:CLOOK",
                "tracks": "number of cylinders (optional for SCAN/CSCAN)",
                "arm": "initial position of the disk head",
                "requests": "list of track requests"
            },
            "payload_example": {
                "algorithm": 1,
                "tracks": 200,
                "arm": 96,
                "requests": [125, 17, 23, 67, 90, 128, 189, 115, 97]
            },
            "description": "This endpoint executes disk scheduling algorithms"
        }
    }

@app.route("/inputs", methods=['GET'])
def list_files():
    """
    Endpoint para listar archivos disponibles en la carpeta `inputs`.
    """
    try:
        files = os.listdir(INPUTS_FOLDER)
        return jsonify({"files": files}), 200
    except Exception as e:
        return jsonify({"error": "Unable to list files", "details": str(e)}), 500


@app.route("/inputs/<filename>", methods=['GET'])
def get_file_content(filename):
    """
    Endpoint para obtener el contenido de un archivo específico en la carpeta `inputs`.
    """
    try:
        filepath = os.path.join(INPUTS_FOLDER, filename)
        if not os.path.exists(filepath):
            return jsonify({"error": f"File {filename} not found"}), 404
        
        # Leer el archivo y devolver su contenido como texto
        with open(filepath, 'r') as file:
            content = file.read()
        
        return jsonify({"content": content}), 200
    except Exception as e:
        return jsonify({"error": "Unable to read file", "details": str(e)}), 500


@app.route("/sched", methods=['POST'])
def sched():
    """
    Endpoint principal para ejecutar algoritmos de planificación.
    """
    try:
        # Verifica si la solicitud incluye un archivo desde el frontend
        if 'file' in request.files:
            file = request.files['file']
            # Leer el contenido del archivo como texto
            lines = file.read().decode('utf-8').splitlines()
        else:
            # Si no es un archivo, asumimos que es JSON
            data = request.get_json()
            algorithm = data.get("algorithm")
            tracks = data.get("tracks")  # Opcional en algunos algoritmos
            arm = data.get("arm")
            requests = data.get("requests")

        # Parseamos el archivo TXT si existe
        if 'file' in request.files:
            # Convertimos el archivo TXT en un diccionario
            data = parse_txt_to_json(lines)
            algorithm = data.get("algorithm")
            tracks = data.get("tracks")
            arm = data.get("arm")
            requests = data.get("requests")

        # Validamos los campos obligatorios
        if not algorithm or arm is None or not requests:
            return jsonify({"error": "Missing required fields: 'algorithm', 'arm', or 'requests'"}), 400

        # Ejecutamos el algoritmo correspondiente
        if algorithm == 1:  # FCFS
            result = fcfs(arm, requests)
        elif algorithm == 2:  # SSTF
            result = sstf(arm, requests)
        elif algorithm == 3:  # SCAN
            result = scan(arm, requests, disk_size=tracks)
        elif algorithm == 4:  # CSCAN
            result = cscan(arm, requests, disk_size=tracks)
        elif algorithm == 5:  # LOOK
            result = look(arm, requests)
        elif algorithm == 6:  # CLOOK
            result = clook(arm, requests)
        else:
            return jsonify({"error": "Invalid algorithm. Use a number between 1 and 6"}), 400

        return jsonify({
            "result": result
        }), 200

    except Exception as e:
        return jsonify({"error": "An error occurred", "details": str(e)}), 500


def parse_txt_to_json(lines):
    """
    Función para convertir un archivo TXT en un objeto JSON.
    """
    payload = {}
    for index, line in enumerate(lines):
        line = line.strip()
        if line.startswith('#') or not line:
            continue  # Ignoramos comentarios y líneas vacías

        if index == 4:
            payload['algorithm'] = int(line)
        elif index == 6:
            payload['tracks'] = int(line)
        elif index == 8:
            payload['arm'] = int(line)
        elif index == 10:
            payload['requests'] = list(map(int, line.split(',')))
    return payload


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)


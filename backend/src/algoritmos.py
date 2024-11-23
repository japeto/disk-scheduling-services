"""
Este algoritmo selecciona la solicitud más cercana a la posición actual del
brazo del disco.
"""


def sstf(request_data):
    requests = sorted(request_data.get('requests', []))
    head_position = request_data.get('head_position', 0)

    # Crear una lista de solicitudes que estarán en orden de ejecución
    seek_order = []
    while requests:
        closest_request = min(requests, key=lambda x: abs(x - head_position))
        seek_order.append(closest_request)
        head_position = closest_request
        requests.remove(closest_request)

    return {"order": seek_order}

"""
En el algoritmo SCAN, el brazo del disco se mueve en una dirección hasta llegar al 
final, y luego invierte la dirección y mueve el brazo en la dirección opuesta, 
atendiendo las solicitudes en ese orden.
"""

def scan(request_data):
    requests = sorted(request_data.get('requests', []))
    head_position = request_data.get('head_position', 0)
    direction = request_data.get('direction', 'left')  # Puede ser 'left' o 'right'

    if direction == 'left':
        requests = [0] + requests[::-1]
    else:
        requests = requests + [100]  # Supongamos que el final del disco es el cilindro 100

    seek_order = []
    for request in requests:
        if (direction == 'left' and request <= head_position) or (direction == 'right' and request >= head_position):
            seek_order.append(request)

    return {"order": seek_order}

"""
El algoritmo C-SCAN es una versión modificada de SCAN donde el brazo del disco, 
al llegar al final, regresa al inicio y continúa atendiendo solicitudes.
"""
def cscan(request_data):
    requests = sorted(request_data.get('requests', []))
    head_position = request_data.get('head_position', 0)

    # Los movimientos en ambas direcciones
    seek_order = [head_position]
    right = [r for r in requests if r > head_position]
    left = [r for r in requests if r < head_position]

    # En dirección a la derecha primero
    seek_order.extend(right)
    # Luego regresa al principio y mueve en dirección contraria
    seek_order.append(max(requests))
    seek_order.extend(left)

    return {"order": seek_order}

"""
El algoritmo LOOK es similar a SCAN, pero no va hasta el final del disco. 
En lugar de eso, el brazo se mueve solo hasta el último cilindro que tiene 
una solicitud.
"""


def look(request_data):
    requests = sorted(request_data.get('requests', []))
    head_position = request_data.get('head_position', 0)
    direction = request_data.get('direction', 'left')

    if direction == 'left':
        requests = [0] + requests[::-1]
    else:
        requests = requests + [100]  # Fin del disco

    seek_order = []
    for request in requests:
        if (direction == 'left' and request <= head_position) or (direction == 'right' and request >= head_position):
            seek_order.append(request)

    return {"order": seek_order}

"""
C-LOOK es una versión modificada del LOOK. Cuando llega al último cilindro en 
la dirección de movimiento, regresa al primer cilindro con una solicitud.
"""


def clook(request_data):
    requests = sorted(request_data.get('requests', []))
    head_position = request_data.get('head_position', 0)

    # Dividir las solicitudes en las dos direcciones
    right = [r for r in requests if r > head_position]
    left = [r for r in requests if r < head_position]

    seek_order = [head_position]
    seek_order.extend(right)
    seek_order.extend(left)

    return {"order": seek_order}

"""
README
# Algoritmos de Planificación del Brazo del Disco

Este proyecto implementa varios algoritmos de planificación del brazo del disco.

## Endpoints

### 1. `/sstf` - Algoritmo SSTF (Shortest Seek Time First)

**Método:** `POST`

**Datos de Entrada:**
```json
{
  "requests": [50, 30, 40, 70, 10],
  "head_position": 35
}

RESPUESTA
.jason
{
  "order": [30, 40, 50, 70, 10]
}

.jason

datos de entrada scan
metodo post
{
  "requests": [50, 30, 40, 70, 10],
  "head_position": 35,
  "direction": "left"
}

salida
{
  "order": [35, 40, 50, 70, 10]
}

datos de entrada look
metood post

{
  "requests": [50, 30, 40, 70, 10],
  "head_position": 35,
  "direction": "right"
}
 salida
 {
  "order": [35, 40, 50, 70, 10]
}

datos de entrada c-look
metodo post
{
  "requests": [50, 30, 40, 70, 10],
  "head_position": 35
}

salida

{
  "order": [35, 40, 50, 70, 10]
}

informacion para probr que  Flask tiene todos los algoritmos de planificación implementados y expuestos a través de endpoints.
Se puede probar usando herramientas como Postman o curl



"""
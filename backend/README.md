
## Overview

This project simulates the following disk scheduling algorithms:
- **FCFS (First Come, First Served)**
- **SSTF (Shortest Seek Time First)**
- **SCAN**
- **C-SCAN**
- **LOOK**
- **C-LOOK**

Users can interact with the API through JSON payloads or upload `.txt` files with predefined formats.

---

## Disk Scheduling Algorithms

1. **FCFS (First Come, First Served):** Requests are served in the order they arrive.
2. **SSTF (Shortest Seek Time First):** The request closest to the current head position is served first.
3. **SCAN:** The disk arm moves in one direction, serving requests until it reaches the end, then reverses.
4. **C-SCAN:** The disk arm moves in one direction, serving requests, then jumps back to the beginning.
5. **LOOK:** Similar to SCAN but only goes as far as the furthest request in each direction.
6. **C-LOOK:** Similar to C-SCAN but jumps back to the start of the furthest request, skipping unused cylinders.

---


# Run backend component

## Without Docker (development mode)

#### Create and activate python environment

1. Inside backend folder:

```
# Create the virtual environment
python -m venv env 
```

or

```
# Create the virtual environment
virtualenv -p python3 env
```

2. Activate python environment

```
# Activate the virtual environment (Linux/Mac)
source env/bin/activate
```

```
# Before activate allow execution (Windows)
Set-ExecutionPolicy RemoteSign
```

```
# Activate the virtual environment (Windows)
env\Scripts\activate
```

#### Install dependencies

With python env activated

```
pip install -r requirements.txt
```

### Run service

With python env activated

```
python src/service.py
```

## Using Dockerfile

1. Inside backend folder, build the image:

```bash
# Replace japeto with your preferred nickname
docker build -t japeto/simbackend .
```

2. Run container with:

```bash
docker run --name simbackend -d -p 0.0.0.0:8000:8000 japeto/simbackend
```

3. Access the backend in your browser:

Open your browser and navigate to:

```plaintext
http://localhost:8000
```

## Unisg Docker Compose

1. From the project root (where docker-compose.yml is located), execute

```bash
docker-compose up --build backend_service
```

2. Access the Services:

- Frontend: http://localhost:3000

Stop the Services:

3. To stop and remove the containers, run:

```bash
docker-compose down
```
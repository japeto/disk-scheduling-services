# Disk scheduling algorithms

Here, an Nginx proxy is set up to route requests to a scheduling service, which is responsible for handling different policies. This ensures efficient routing and load balancing between services.

## Project Structure

The project follows this structure:

```
.
├── backend/
│   ├── inputs/            # Input files folder
│   ├── src/               # Backend source code
│   │   ├── service.py    # Main Flask application
│   │   ├── fcfs.py       # FCFS algorithm implementation
│   │   ├── sstf.py       # SSTF algorithm implementation
│   │   ├── scan.py       # SCAN algorithm implementation
│   │   ├── cscan.py      # C-SCAN algorithm implementation
│   │   ├── look.py       # LOOK algorithm implementation
│   │   ├── clook.py      # C-LOOK algorithm implementation
│   ├── requirements.txt  # Python dependencies
│   ├── Dockerfile        # Backend Dockerfile
│   ├── ...               # Other files 
├── frontend/
│   ├── public-html/      # Frontend source code
│   ├── Dockerfile        # Frontend Dockerfile
│   ├── ...               # Other files 
├── proxy/
│   ├── nginx              
│   ├── ...               # Other files      
├── docker-compose.yml    # Docker Compose configuration

```


## How to Run the Project

1. Build and start the services:

From the root directory, execute the following command:

```bash
docker-compose up --build
```

2. Access the application:

- Frontend: Open your browser and go to http://localhost:3000
- Backend API (if exposed): Access via http://localhost:8000

3. Stop the services:
To stop and remove the containers, run:

```bash
docker-compose down
```


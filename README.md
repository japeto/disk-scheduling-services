Leonardo Rios - 2310129 Laura Celeste Berrio - 2322101 Juan Pablo Montealegre - 2310041

# Disk scheduling algorithms

Here, an Nginx proxy is set up to route requests to a scheduling service, which is responsible for handling different policies. This ensures efficient routing and load balancing between services.

## Project Structure

The project follows this structure:

```graphql
disk-scheduling-services/
├── docker-compose.yml
├── backend/
│   ├── Dockerfile
│   ├── src/  # Service code
│   │   ├──service.py
│   │   ├──fcfs.py
│   │   ├──sstf.py
│   │   ├──scan.py
│   │   ├──cscan.py
│   │   ├──look.py
│   │   ├──clook.py
│   ├── inputs   # Other files
│   │   ├──dsa001.json
│   │   ├──dsa002.json
│   │   ├──dsa003.json
│   │   ├──dsa004.json
│   │   ├──dsa005.json
│   │   ├──dsa006.json
│   │   ├──dsa007.json
│   │   ├──dsa008.json
│   │   ├──dsa009.json
│   │   ├──dsa010.json
├── frontend/
│   ├── Dockerfile
│   ├── public-html/  # HTML code
├── proxy/
│   ├── Dockerfile
│   ├── nginx.conf
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


# Integrantes
- Luis Felipe Garcia 2343105
- Keyner Meneses 2341611
- Mateo Noguera 2342673

# Video
Enlace: 


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
│   ├── ...   # Other files
├── frontend/
│   ├── Dockerfile
│   ├── public-html/  # HTML code
│   ├── ...   # Other files
├── proxy/
│   ├── Dockerfile
│   ├── nginx.conf
│   ├── ...   # Other files
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


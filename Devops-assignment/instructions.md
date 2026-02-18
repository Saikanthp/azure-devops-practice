# Local Development Instructions

## Prerequisites
- Docker Desktop (v24+)
- Docker Compose v2

## Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/<your-username>/devops-assignment.git
cd devops-assignment
```

### 2. Create your env file
```bash
cp .env.example .env
# Edit .env if needed
```

### 3. Build images
```bash
docker compose build
```

### 4. Start the full stack
```bash
docker compose up -d
```

### 5. Access services
| Service  | URL |
|----------|-----|
| Frontend | http://localhost:3000 |
| API Docs | http://localhost:8000/docs |
| API Root | http://localhost:8000 |

### 6. View logs
```bash
docker compose logs -f          # all services
docker compose logs -f backend  # just backend
docker compose logs -f worker   # just celery worker
```

### 7. Debug a specific container
```bash
docker compose exec backend bash
```

### 8. Stop everything
```bash
docker compose down
```

### 9. Full reset (including volumes)
```bash
docker compose down -v --remove-orphans
```
# Journey – DevOps Assessment

## Approach
Starting from the given FastAPI + Celery + Redis app, I:

1. **Containerized** each service (backend API, Celery worker, Redis, Nginx/frontend).
2. **Eliminated all hardcoded values** – moved broker URLs, CORS origins, sleep durations into env vars.
3. **Docker Compose** provides a one-command local stack.
4. **Terraform (IaC)** provisions VPC, ECS Fargate, ElastiCache Redis, and ALB on AWS — zero manual clicks.
5. **GitHub Actions CI/CD** lints on every PR, then builds/pushes the Docker image to GHCR and runs `terraform apply` on merge to main.

## Key Decisions
- **ECS Fargate** → no server management; scales easily.
- **ElastiCache Redis** → managed, HA Redis instead of self-hosted.
- **CloudWatch Logs** → native AWS logging, no extra tooling.
- **GHCR** → free image registry tightly integrated with GitHub Actions.
- **ALB health check** → `/health` endpoint ensures zero-downtime deploys.

## Challenges
- Celery needs `AsyncResult` to use the same backend URL as the broker — solved via single `REDIS_URL` env var.
- ECS Fargate requires `awsvpc` networking; security groups must allow port 6379 from the task SG to Redis SG.
# Architecture Diagram
```
┌──────────────────────────────────────────────────────┐
│                        AWS Cloud                      │
│                                                      │
│   ┌──────────┐    ┌────────────────────────────────┐ │
│   │  User    │───▶│  Application Load Balancer     │ │
│   │ Browser  │    │  (port 80, public)             │ │
│   └──────────┘    └────────────┬───────────────────┘ │
│                                │                      │
│                   ┌────────────▼───────────────────┐ │
│                   │   ECS Fargate – Backend         │ │
│                   │   FastAPI :8000                 │ │
│                   │   (CloudWatch Logs)             │ │
│                   └────────────┬───────────────────┘ │
│                                │ REDIS_URL            │
│                   ┌────────────▼───────────────────┐ │
│                   │   ElastiCache (Redis 7)         │ │
│                   │   Managed broker + result store │ │
│                   └────────────┬───────────────────┘ │
│                                │ REDIS_URL            │
│                   ┌────────────▼───────────────────┐ │
│                   │   ECS Fargate – Celery Worker   │ │
│                   │   (CloudWatch Logs)             │ │
│                   └────────────────────────────────┘ │
│                                                      │
│   GitHub Actions CI/CD ──▶ GHCR ──▶ ECS Deploy      │
│   Terraform state stored in S3                       │
└──────────────────────────────────────────────────────┘
```
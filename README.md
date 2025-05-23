# MadeByParm Portfolio

This repository contains a full-stack portfolio site built with React (Vite) and Django REST Framework.

## Local Development

Requirements:
- Docker and docker-compose

```bash
# Build and start services
docker-compose up --build
```

Frontend will be available at `http://localhost:3000` and backend API at `http://localhost:8000`.

## Production

Create an `.env` file with production settings and run:

```bash
docker-compose -f docker-compose.yml up --build -d
```

Configure a reverse proxy (NGINX, Caddy, etc.) to forward traffic to the frontend and backend containers.

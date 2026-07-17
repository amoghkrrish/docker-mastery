## Docker Mastery – Learning Log ##########

## Day 1 – Foundations: Hello World & Nginx

### What I learned
- Docker architecture: daemon, images, containers.
- Running my first container: `docker run hello-world`.
- Running a web server (nginx) in detached mode with port mapping (`-p`).
- Bind mounts (`-v`) to serve custom HTML from my Mac.
- Basic container lifecycle: `ps`, `stop`, `start`, `logs`, `exec`, `rm`.

### Hands‑on
- Pulled and ran the `hello-world` image.
- Ran an nginx container accessible at `http://localhost:8080`.
- Mounted a local `html/` directory and saw my own `index.html` served.
- Practiced stopping, restarting, viewing logs, and removing containers.

### Repository
All code and notes for this day are in the `day1-hello-world/` folder.

# Docker Day 2 – Building Custom Images

## What I learned
- Writing a Dockerfile with `FROM`, `COPY`, `EXPOSE`, `CMD`.
- Building an image with `docker build -t <name>:<tag> .`.
- Running a custom nginx container that serves my HTML.
- How Docker caches layers to speed up builds.
- Tagging and pushing an image to Docker Hub (optional).

## Files
- `Dockerfile` – the recipe for the image.
- `html/index.html` – the custom web page.

# Docker Day 3 – Custom Python App with Environment Variables

## What I learned
- Using `python:3-alpine` as a base image.
- `WORKDIR` to set the working directory.
- `ENV` for default environment variables.
- Passing environment variables at runtime with `-e`.
- The difference between `ENV` in Dockerfile and `-e` at `docker run`.
- Basic Python HTTP server that uses environment variables.

## Files
- `app.py` – a simple web server that displays a configurable message.
- `Dockerfile` – builds the image.

# Docker Day 4 – Multi‑Container App with Docker Compose

## What I learned
- Writing a `docker-compose.yml` file with two services.
- How services communicate using the service name as hostname.
- `depends_on` to order container startup.
- `environment` to pass configuration.
- Using a pre‑built image (`redis:alpine`) alongside a custom one.
- Basic Flask + Redis counter app.
- Compose commands: `up`, `down`, `ps`, `logs`, `exec`.

## Files
- `app.py` – Flask app that increments a Redis counter.
- `Dockerfile` – builds the web app image.
- `docker-compose.yml` – defines the multi‑container setup.

# Docker Day 5 – Persistent Data & Health Checks

## What I learned
- Named volumes keep data across container removals.
- `volumes:` in Compose to define and mount a named volume.
- Redis data stored in a volume survives `docker-compose down`.
- `HEALTHCHECK` in Dockerfile with `curl` to monitor app health.
- Docker automatically restarts unhealthy containers (with restart policy).
- Testing persistence by restarting containers.

## Files
- `app.py` – Flask app (unchanged).
- `Dockerfile` – added `curl` and `HEALTHCHECK`.
- `docker-compose.yml` – added `redis_data` volume.

# Docker Day 6 – Multi‑Stage Builds with Python & Docker Hub

## What I learned
- How to use a multi‑stage Dockerfile to separate build and runtime environments.
- Using `COPY --from=builder` to copy only the virtual environment and app code.
- Reduced final image size by excluding build tools.
- Published a Python Flask image to Docker Hub.

## Files
- `app.py` – a simple Flask web server.
- `Dockerfile` – multi‑stage build (builder + final).
- `requirements.txt` – only Flask (can be extended).

## Docker Hub
- Image: `amoghkrrish/python-multi-stage` (tags: v1, latest)

# Docker Day 7 – Custom Networks, Isolation & Security Scanning

## What I learned
- Creating and using custom Docker networks to segment services.
- How to place services on multiple networks (web on frontend + backend).
- Isolating internal services (worker) by not exposing ports and using a private network.
- Using `docker scout` to scan images for vulnerabilities.

## Architecture
- **web** – public, on frontend + backend.
- **worker** – internal, only on backend.
- **redis** – internal, only on backend.
- **frontend** network – exposed to host.
- **backend** network – private, no external access.

## Files
- `web_app.py`, `worker.py` – Python services.
- `Dockerfile` – builds both services.
- `docker-compose.yml` – defines the multi‑network setup.

# Docker Day 8 – Resource Limits

## What I learned
- How to limit a container’s memory with the `--memory` flag.
- What happens when a container tries to use more memory than allowed (OOM kill by the kernel, signal 9).
- How to use the `stress` tool to test memory limits.
- How to read and fix common flag syntax errors (`invalid suffix`).

## Commands

### Run within memory limit (success)
```bash
docker run --rm -it --name stress-test --memory=50m polinux/stress stress --vm 1 --vm-bytes 40M --timeout 10
-DOCKER

# Docker Day 9 – Production Compose

## What I learned
- Using `.env` files to manage environment variables in Docker Compose.
- Setting resource limits (`deploy.resources.limits`) for containers.
- Using Docker secrets to securely inject sensitive data (passwords, API keys).
- Making a Flask app read secrets from the mounted secret file.
- Proper `.gitignore` to avoid committing secrets.

## Files
- `app.py` – Flask web app that reads a secret and connects to Redis.
- `Dockerfile` – builds the web image.
- `requirements.txt` – Python dependencies.
- `.env` – environment variables (not committed).
- `my_secret.txt` – the secret (not committed).
- `docker-compose.yml` – production‑style Compose file with limits and secrets.

## Commands
```bash
docker-compose up -d         # start
docker-compose ps            # check status
docker-compose exec web cat /run/secrets/my_secret  # view secret
docker-compose down          # stop and clean up

# Docker Day 10 – Networking Deep‑Dive

## What I learned
- Default bridge vs user‑defined bridge: DNS resolution works only on user‑defined networks.
- How to create a custom bridge network and communicate by container name.
- The embedded DNS server at `127.0.0.11`.
- Host network mode (shares the host’s network stack).
- None network mode (complete isolation).
- Overlay networks for multi‑host communication (Swarm).
- How to connect a container to multiple networks.

## Commands used

### Custom bridge & DNS
```bash
docker network create --driver bridge my-net
docker run -dit --name web --network my-net nginx:alpine
docker run -dit --name client --network my-net alpine
docker exec client ping web   # works
docker network inspect my-net

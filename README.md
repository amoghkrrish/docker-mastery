# Docker Mastery – Learning Log

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

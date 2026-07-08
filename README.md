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

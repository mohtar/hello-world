Simple hello world app written in Python/AIOHTTP.

Included is a sample CI/CD config file for CircleCI. Commits made to this repository are automatically built as Docker image and pushed to a Docker registry.

A Docker Compose config is also provided for local environments. Simply run `docker-compose up --build`.

The endpoint `/actuator/health` is provided for health checks.

# Containerized Web App

![CI](https://github.com/femurkufoin-jpg/containerized-web-app/actions/workflows/ci.yml/badge.svg)

A simple Flask web application built to practice a practical DevOps workflow: application development, testing, Docker containerization, Docker Compose, Redis, and GitHub Actions CI/CD.

## What the Project Does

The application provides two simple endpoints:

- `/health` - returns the health status of the application.
- `/visits` - increments and returns a visit counter stored in Redis.

The application is built with Python and Flask, while Redis is used as the supporting data service.

The project demonstrates how an application can be developed, tested, containerized, run with a supporting service, and automatically tested and built using CI/CD.

## Technologies Used

- Python 3.13
- Flask
- Redis
- Docker
- Docker Compose
- Pytest
- Flake8
- GitHub Actions
- GitHub Container Registry (GHCR)

## Project Structure

```text
containerized-web-app/
.github/
    workflows/
        ci.yml
app/
    __init__.py
    routes.py
tests/
    test_app.py
.dockerignore
.env.example
.gitignore
Dockerfile
docker-compose.yml
README.md
requirements.txt
```

## Prerequisites

Before running the application locally, make sure you have the following installed:

- Python 3.13
- Git
- Docker Desktop
- Docker Compose

For local development without Docker, Python and the required Python packages are needed.

## Running Locally Without Docker

1. Clone the repository:

```bash
git clone https://github.com/femurkufoin-jpg/containerized-web-app.git
cd containerized-web-app
```

2. Create and activate a virtual environment:

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

3. Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

4. Start the Flask application:

```bash
python -m flask --app app run --host=0.0.0.0 --port=5000
```

The application will be available at:

```text
http://localhost:5000
```

The `/health` endpoint can be tested at:

```text
http://localhost:5000/health
```

The `/visits` endpoint can be tested at:

```text
http://localhost:5000/visits
```

> Note: The `/visits` endpoint uses Redis as its supporting data service when running the complete application with Docker Compose.

## Running With Docker

Build the Docker image:

```bash
docker build -t containerized-web-app .
```

Run the container:

```bash
docker run -p 5000:5000 containerized-web-app
```

The application can then be accessed at:

```text
http://localhost:5000
```

## Running With Docker Compose

Docker Compose is used to run the Flask application together with Redis.

Start the services:

```bash
docker compose up --build
```

The application will be available at:

```text
http://localhost:5000
```

Test the health endpoint:

```text
http://localhost:5000/health
```

Test the visits endpoint:

```text
http://localhost:5000/visits
```

The visit counter is stored in Redis.

To stop the services:

```bash
docker compose down
```

To stop the services and remove the named volume:

```bash
docker compose down -v
```

## Redis Persistence

Redis is used as the supporting data service for the `/visits` endpoint.

A named Docker volume is used to persist Redis data. This allows the visit counter data to remain available when the Redis container is recreated, depending on whether the volume is removed.

The Docker Compose configuration also uses a Redis health check so that the application starts after Redis is ready.

## Testing

The project uses Pytest for automated tests.

Run the tests with:

```bash
python -m pytest
```

The tests verify the application's basic functionality, including the health and visits endpoints.

## Code Quality

Flake8 is used to check the Python code for style and potential issues.

Run Flake8 with:

```bash
python -m flake8 app tests
```

## CI/CD Pipeline

GitHub Actions is used to automatically test and build the application.

The workflow is located at:

```text
.github/workflows/ci.yml
```

The CI pipeline performs automated checks when changes are pushed to the repository or when a pull request is created.

The pipeline includes steps for:

1. Checking out the repository.
2. Setting up Python.
3. Installing project dependencies.
4. Running Flake8.
5. Running Pytest.
6. Building the Docker image.
7. Building and publishing the container image to GitHub Container Registry (GHCR) when the workflow conditions are met.

The CI status can be viewed from the GitHub Actions tab of the repository.

## GitHub Container Registry

The project uses GitHub Container Registry (GHCR) to store the Docker image produced by the CI workflow.

This demonstrates how a containerized application can be automatically built and published as part of a CI/CD workflow.

## Troubleshooting

### Flask import error

During the Docker Compose setup, the application container initially exited because Flask could not import `register_routes` from `app.routes`.

The problem was caused by a mismatch between `app/__init__.py` and `routes.py`. The `__init__.py` file was importing `register_routes`, while the current `routes.py` exposed `create_app`.

The import was corrected so that the application used the function actually defined in `routes.py`.

After the correction, the application container started successfully.

### Flake8 command not recognized

During CI troubleshooting, Flake8 was initially not recognized in the local environment.

The issue was resolved by installing Flake8 with:

```bash
python -m pip install flake8
```

Flake8 was then run with:

```bash
python -m flake8 app tests
```

This exposed additional code-quality issues that were corrected before the CI workflow was finalized.

### Redis and Docker Compose

Redis was configured as a supporting service for the application.

A health check was added to Redis, and the application was configured to depend on Redis being healthy before starting.

This helped ensure that the application did not attempt to use Redis before the Redis service was ready.

## Conclusion

This project demonstrates a practical DevOps workflow from application development to testing, containerization, service orchestration, and CI/CD automation.

The project provided hands-on practice with Flask, Redis, Docker, Docker Compose, Pytest, Flake8, GitHub Actions, and GitHub Container Registry.
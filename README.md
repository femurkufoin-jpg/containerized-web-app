# Containerized Web App

[![CI](https://github.com/femurkufoin-jpg/containerized-web-app/actions/workflows/ci.yml/badge.svg)](https://github.com/femurkufoin-jpg/containerized-web-app/actions/workflows/ci.yml)

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
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
├── app/
│   ├── __init__.py
│   └── routes.py
│
├── tests/
│   └── test_app.py
│
├── .dockerignore
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
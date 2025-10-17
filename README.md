# Lunch Decision Service

Lunch Decision Service is an internal tool designed to help employees decide where to have lunch. Restaurants upload daily menus through the system API, and employees vote for the menu they prefer. 
The service supports multiple versions of the mobile app and is built with maintainability and readability in mind.

## Features

- **Authentication**: JWT-based authentication for employees.
- **Restaurants Management**: Create and manage restaurants.
- **Menu Management**: Upload daily menus for each restaurant.
- **Employee Management**: Register and manage employees.
- **Voting System**: Employees can vote for menus on specific days.

## Project Structure

- `users/` — custom user model and employee management.
- `votes/` — voting system with vote events and vote items.
- `.env` — environment configuration for local development and Docker.
- `wait_for_db.sh` — script to wait until the database is ready.
- `Dockerfile` and `docker-compose.yml` — containerized deployment setup.

## Getting Started

### Local Development

The project can be run locally using SQLite. Developers should set up environment variables, apply database migrations, and start the Django development server.

### Docker Setup

For containerized deployment, the project uses PostgreSQL in Docker. Environment variables must be configured for Docker, the `wait_for_db.sh`script ensures the database is ready, and the server starts automatically after migrations.

### Run using docker compose

```bash
python manage.py makemigrations
docker compose up --build
```

### Run local using SQLite

```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

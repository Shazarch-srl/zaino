# Zaino

A simple Django project for planning your hiking or climbing gear. Select equipment items and calculate total weight.

## Development Setup (Docker)

1. Build and start services:

```bash
docker-compose up --build
```

2. Access the app at [http://localhost:8000](http://localhost:8000).

Database migrations are run automatically on start. After the container boots,
load the initial dataset:

```bash
docker compose exec web python manage.py loaddata initial_data.json
```

This fixture also creates an admin user (`admin`/`admin`).

## Production Build

Build the image using the production Dockerfile:

```bash
docker build -t zaino .
```

Run the container with proper environment variables and mount a volume for `db.sqlite3` if needed:

```bash
docker run -p 8000:8000 zaino
```

## Usage

Create categories and items in the Django admin interface (`/admin`). Then select items on the home page to compute your pack weight.

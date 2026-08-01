# FastAPI-starter

A FastAPI starter template with async SQLAlchemy 2, Alembic migrations, and a PostgreSQL database running in Docker.

## Requirements

- Install [UV](https://docs.astral.sh/uv/#installation)
- Python 3.14, installed with `uv python install 3.14`
- Install [Docker Desktop](https://www.docker.com/products/docker-desktop)

## Setup guide

```bash
uv sync                  # install dependencies
cp .env.example .env     # database config
docker compose up -d     # start PostgreSQL
```

Define your models in `app/models` and import each module in `app/models/__init__.py` — otherwise Alembic won't detect them:

```python
from app.models import users as users
```

Once the models are in place, generate and apply the first migration:

```bash
uv run alembic revision --autogenerate -m "init"
uv run alembic upgrade head
```

Run the app:

```bash
uv run fastapi dev
```

Interactive docs: http://localhost:8000/docs

## Development

Format and lint:

```bash
uv run ruff format
uv run ruff check
```

Generate a migration from model changes, apply it, revert one revision, or roll everything back:

```bash
uv run alembic revision --autogenerate -m "msg"
uv run alembic upgrade head

uv run alembic downgrade -1
uv run alembic downgrade base
```

The migration environment in `migrations/` was created with the async template — one-time setup, already done, kept here for reference:

```bash
uv run alembic init -t async migrations
```

Open a psql shell, check the database container, or stop it and wipe the data:

```bash
docker compose exec postgres psql -U postgres -d devdb
docker compose exec postgres pg_isready

docker compose down -v
```

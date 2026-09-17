.PHONY: setup install migrate collectstatic build render-start tailwind-build tests

setup:
	make install

install:
	uv sync --dev

migrate:
	uv run python manage.py migrate

collectstatic:
	uv run python manage.py collectstatic --noinput

build:
	./build.sh

render-start:
	uv run gunicorn task_manager.wsgi

tailwind-build:
	uv run python manage.py tailwind build

tests:
	uv run pytest --cov --cov-report=term --cov-fail-under=80
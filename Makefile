install:
	uv sync

migrate:
	uv run django-admin migrate

collectstatic:
	uv run django-admin collectstatic --noinput

build:
	./build.sh

render-start:
	gunicorn task_manager.wsgi
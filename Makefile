export COMPOSE_DOCKER_CLI_BUILD=1
export DOCKER_BUILDKIT=1

all:
	down build up

up:
	docker-compose up

down:
	docker-compose down --remove-orphans

build:
	docker-compose build


shell:
	docker-compose exec cloneflix python manage.py shell

migrate:
	docker-compose exec cloneflix python manage.py migrate

makemigrations:
	docker-compose exec cloneflix python manage.py makemigrations

createsuperuser:
	docker-compose exec cloneflix python manage.py createsuperuser
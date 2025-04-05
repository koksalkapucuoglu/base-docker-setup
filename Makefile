build:
	docker compose --env-file .env build

run:
	docker compose --env-file .env up

down:
	docker compose down

makemigrations:
	docker compose run app python manage.py makemigrations

migrate:
	docker compose run app python manage.py migrate

user:
	docker compose run app python manage.py createsuperuser

build_force:
	docker compose --env-file .env build --no-cache

run_command:
	docker compose run app python manage.py $(command)
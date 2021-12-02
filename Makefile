default: run

run:
	docker-compose -f "docker-compose.yml" up -d

build:
	docker-compose -f "docker-compose.yml" up --build
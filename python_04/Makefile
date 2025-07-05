SERVICE_NAME = python_04
COMPOSE_FILE = ./infra/docker-compose.yml

all: up

up:
	@docker-compose -f $(COMPOSE_FILE) up --build -d

down:
	@docker-compose -f $(COMPOSE_FILE) down

fclean:
	@docker-compose -f $(COMPOSE_FILE) down --rmi all -v

shell:
	@docker-compose -f $(COMPOSE_FILE) exec $(SERVICE_NAME) /bin/bash

logs:
	@docker-compose -f $(COMPOSE_FILE) logs -f

re: fclean all

.PHONY: all up down fclean shell logs re

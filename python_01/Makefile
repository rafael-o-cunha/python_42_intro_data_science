SHELL := /bin/bash

SERVICE_NAME = py01
COMPOSE_FILE = ./infra/docker-compose.yml
DELIVERY_DIR = py01

all: up

up:
	@docker-compose -f $(COMPOSE_FILE) up --build -d

down:
	@docker-compose -f $(COMPOSE_FILE) down

fclean:
	@docker-compose -f $(COMPOSE_FILE) down --rmi all -v

shell:
	@docker exec -it $(SERVICE_NAME) /bin/bash

test:
	@echo "---TEST EX00----------------------------------"
	@docker exec -it $(SERVICE_NAME) /bin/bash -c "cd /app/ex00 && python -m unittest test_give_bmi.py"

	@echo "---TEST EX01----------------------------------"
	@docker exec -it $(SERVICE_NAME) /bin/bash -c "cd /app/ex01 && python -m unittest test_array2D.py"

	@echo "---TEST EX02----------------------------------"
	@docker exec -it $(SERVICE_NAME) /bin/bash -c "cd /app/ex02 && python -m unittest test_load_image.py"

	@echo "---TEST EX03----------------------------------"
	@docker exec -it $(SERVICE_NAME) /bin/bash -c "cd /app/ex03 && python -m unittest test_load_image.py test_zoom.py test_zoom_program.py"

	@echo "---TEST EX04----------------------------------"
	@docker exec -it $(SERVICE_NAME) /bin/bash -c "cd /app/ex04 && python -m unittest test_load_image.py test_rotate.py test_rotate_program.py"

	@echo "---TEST EX05----------------------------------"
	@docker exec -it $(SERVICE_NAME) /bin/bash -c "cd /app/ex05 && python -m unittest test_load_image.py test_pimp_image.py test_pimp_image_program.py"


# --- norminette / deliver -----------------------------------------------
# Single source of truth for the "Files to turn in" of each exercise
# (per the subject PDF). Reused by both `norminette` and `deliver`.
NORM_ex00 = ex00/give_bmi.py
NORM_ex01 = ex01/array2D.py
NORM_ex02 = ex02/load_image.py
NORM_ex03 = ex03/load_image.py ex03/zoom.py
NORM_ex04 = ex04/load_image.py ex04/rotate.py
NORM_ex05 = ex05/load_image.py ex05/pimp_image.py

norminette:
	@echo "---NORMINETTE-----------------------------------"
	@docker exec $(SERVICE_NAME) /bin/bash -c '\
		set -u; \
		cd /app; \
		GREEN="\033[0;32m"; RED="\033[0;31m"; NC="\033[0m"; \
		declare -A FILES=( \
			[ex00]="$(NORM_ex00)" \
			[ex01]="$(NORM_ex01)" \
			[ex02]="$(NORM_ex02)" \
			[ex03]="$(NORM_ex03)" \
			[ex04]="$(NORM_ex04)" \
			[ex05]="$(NORM_ex05)" \
		); \
		STATUS=0; \
		for ex in ex00 ex01 ex02 ex03 ex04 ex05; do \
			if flake8 $${FILES[$$ex]}; then \
				printf "$${GREEN}[OK]   %s$${NC}\n" "$$ex"; \
			else \
				printf "$${RED}[FAIL] %s$${NC}\n" "$$ex"; \
				STATUS=1; \
			fi; \
		done; \
		echo "--------------------------------------------------"; \
		if [ $$STATUS -eq 0 ]; then \
			printf "$${GREEN}norminette: all exercises OK$${NC}\n"; \
		else \
			printf "$${RED}norminette: violations found$${NC}\n"; \
		fi; \
		exit $$STATUS \
	'

deliver:
	@echo "---PREPARING DELIVERY----------------------------"
	@rm -rf $(DELIVERY_DIR)
	@GREEN="\033[0;32m"; RED="\033[0;31m"; NC="\033[0m"; \
	declare -A FILES=( \
		[ex00]="$(NORM_ex00)" \
		[ex01]="$(NORM_ex01)" \
		[ex02]="$(NORM_ex02)" \
		[ex03]="$(NORM_ex03)" \
		[ex04]="$(NORM_ex04)" \
		[ex05]="$(NORM_ex05)" \
	); \
	STATUS=0; \
	for ex in ex00 ex01 ex02 ex03 ex04 ex05; do \
		mkdir -p $(DELIVERY_DIR)/$$ex; \
		if cp $${FILES[$$ex]} $(DELIVERY_DIR)/$$ex/ 2>/tmp/deliver_err.$$$$; then \
			N=$$(echo $${FILES[$$ex]} | wc -w); \
			printf "$${GREEN}[OK]   %s (%s file(s) copied)$${NC}\n" "$$ex" "$$N"; \
		else \
			printf "$${RED}[FAIL] %s -> $$(cat /tmp/deliver_err.$$$$)$${NC}\n" "$$ex"; \
			STATUS=1; \
		fi; \
		rm -f /tmp/deliver_err.$$$$; \
	done; \
	echo "--------------------------------------------------"; \
	if [ $$STATUS -eq 0 ]; then \
		printf "$${GREEN}delivery ready at ./$(DELIVERY_DIR)$${NC}\n"; \
	else \
		printf "$${RED}delivery incomplete - fix the missing files above$${NC}\n"; \
	fi; \
	exit $$STATUS

delivery-clean:
	@echo "---CLEANING DELIVERY------------------------------"
	@rm -rf $(DELIVERY_DIR)
	@echo "delivery folder removed (./$(DELIVERY_DIR))"
	
logs:
	@docker-compose -f $(COMPOSE_FILE) logs -f

re: fclean all

.PHONY: all up down fclean shell logs re test norminette deliver
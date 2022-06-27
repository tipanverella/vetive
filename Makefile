CC=poetry
PYTHONFILES=vetive
GIT=git


install:
	$(CC) install

lint: $(PYTHONFILES) $(ACTIONS)
	$(CC) run black $(PYTHONFILES)
	$(CC) run pylint $(PYTHONFILES)

build: $(PYTHONFILES) coverage
	$(CC) update
	$(CC) export --format requirements.txt --without-hashes --output requirements.txt
	$(CC) build

test: 
	poetry run pytest -vv

coverage:
	poetry run pytest -vv --cov=dsa_utils --cov-report=term --cov-report=html

push: lint build
	$(CC) version patch
	$(GIT) add -A
	$(GIT) commit -m "$(CM)"
	$(GIT) push origin


.PHONY: lint build

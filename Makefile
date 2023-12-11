test:
	pytest src/

lint:
	ruff check src/

format:
	ruff format src/

build: format types test

types:
	mypy src/

deps:
	pipenv update
	pipenv requirements --dev > requirements.txt

run:
	python src/main.py

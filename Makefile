test:
	pytest src/

format:
	ruff format src/

types:
	mypy src/

build: format types test

deps:
	pipenv update
	pipenv requirements --dev > requirements.txt

run:
	python src/main.py

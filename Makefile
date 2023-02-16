all:
	pip install -r requirements.txt
	python -m cake_aligner

test:
	pytest tests/
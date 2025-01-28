VENV = venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
PYTEST = $(VENV)/bin/pytest

.PHONY: venv install test clean clean-venv
venv:
	python3 -m venv $(VENV)
	$(PIP) install --upgrade pip

install: venv
	$(PIP) install -r requirements.txt

test: venv
	$(PYTHON) -m pytest tests/

clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete

clean-venv:
	rm -rf $(VENV)

# Makefile for Python project

# Define variables
PYTHON = python3.10
SRC_DIR = .
TEST_DIR = ../tests
VENV_DIR = ../env
VENV_ACTIVATE = $(VENV_DIR)/bin/activate

# Default target
.PHONY: all
all: $(VENV_DIR) install test pack #run

# Create virtual environment
$(VENV_DIR):
	$(PYTHON) -m venv $(VENV_DIR)

# Install dependencies
.PHONY: install
install: $(VENV_DIR) $(VENV_ACTIVATE)
	. $(VENV_ACTIVATE); sudo pip install -r ../requirements.txt

# Run tests
.PHONY: test
test: $(VENV_DIR) $(VENV_ACTIVATE)
	chmod +x $(VENV_ACTIVATE); . $(VENV_ACTIVATE); cd $(TEST_DIR) && pytest .

# Run Calculator
.PHONY: run
run: $(VENV_ACTIVATE)
	$(PYTHON) ./main.py

# Pack files
.PHONY: pack
pack: $(VENV_DIR) $(VENV_ACTIVATE)
	chmod +x $(VENV_ACTIVATE); . $(VENV_ACTIVATE); cd .. ;sudo zip xnovot2q_xvarsa01_xperec00_247112.zip -r $(CURDIR)/*

# Clean up
.PHONY: clean
clean:
	rm -rf $(VENV_DIR)
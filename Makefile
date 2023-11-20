venv:
	@echo "Create a new Virtual environment"
	@python3 -m venv venv

activate:
	@echo "Activate virtual environment"
	@source venv/bin/activate

install:
	@echo "Install dependencies"
	@pip install -r requirements.txt

run:
	@echo "Running application..."
	@streamlit run main.py

.PHONY: help
.DEFAULT_GOAL := help

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

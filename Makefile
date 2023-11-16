clean_setup:
	pyenv install -s $(shell cat .python-base-version)
	pyenv virtualenv-delete -f $(shell cat .python-version) || true
	pyenv virtualenv $(shell cat .python-base-version) $(shell cat .python-version)
	make setup
	pre-commit install
	pyenv version

setup:
	pip install -r requirements.txt

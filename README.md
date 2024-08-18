# Usual data project structure

## Pre requisites:
1. python
2. pyenv
3. poetry

## Instaling libraries and virtual environment

In project folder
1. `pyenv install 3.12.5`
2. `poetry env use 3.12.5`
3. `poetry shell`
4. `poetry install`

Your virtual environment and depenencies should be installed and running.

## Running the project

1. python main.py


## Additional info

1. isort usage to order imports -> on root folder `isort .`
2. blue used to format python code -> on root folder `blue .`
3. adding to pyproject.toml to allow black to be the main formatter. 
`[tool.isort]
profile = "black"
known_third_party = []`


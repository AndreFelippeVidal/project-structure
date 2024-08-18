# Data Project Structure

Project initial documentation: [Data Project Initial Structure](https://AndreFelippeVidal.github.io/project-structure/)

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

1. `python project_structure/main.py`


## Additional info (optional)

1. isort usage to order imports -> on root folder `isort .`
2. blue used to format python code -> on root folder `blue .`
3. adding to pyproject.toml to allow black to be the main formatter.
`[tool.isort]
profile = "black"
known_third_party = []`
4. pydocstyle used to check which modules, packages or funtions doesn't have a docstring. `pydocstyle .`
5. do vulnerabiluty checks on the installed libraries `pip-audit`
6. taskipy to automate all the tasks that we want the code to perform, this is done with poetry. (pyproject.toml)
    - [tool.taskipy.tasks]
    - format = "isort . && blue ."
    - after adding to poetry file, run `task format`
7. mkdocs -> very useful for documentation instead of confluence. follows the row to use.
    - If you want anything specific as theme or any other change you can find directly on mkdocs page.
    - Dependencies: `poetry add mkdocs mkdocstrings-python pygments mkdocs-material pymdown-extensions`
    1. `mkdocs new .` -> on root folder, created the docs folder with the starting files
    2. `mkdocs serve` -> shows on logs the page of the docs, need to click on the http://127.0.0.1:8000/
    3. `mkdocs build` -> create the strucutre for a website if you want to deploy somewhere else
    4. `mkdocs gh-deploy` -> to deploy the page to github pages
    5. with taskipy we added a task called kill to kill what is running on port 8000 with `task kill`
8. pre-commit -> `poetry add pre-commit`
    1. Need to create `.pre-commit-config.yaml` on project root folder.(pre-commit docs)[https://pre-commit.com/]
    2. `pre-commit install`
    3. every commit will only be done if follows those best practices defined in pre-commit-config file.
    4. `pre-commit uninstall`
    5. `poetry remove pre-commit`

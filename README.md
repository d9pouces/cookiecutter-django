Cookiecutter Django
===================

Generate a skeleton of a Django project with the following attributes:

- based on poetry and configuration in pyproject.toml
- Dockerfile/compose.yaml files ready for development
- run configurations for runserver/unit testing in PyCharm
- pre-commit hookes installed and configured
- examples of working unittests
- copyright notices configured for PyCharm
- example of Github workflow for unittests

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter gh:d9pouces/cookiecutter-django

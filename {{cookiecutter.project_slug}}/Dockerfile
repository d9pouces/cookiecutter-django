FROM python:3.11
ENV PYTHONUNBUFFERED 1
ADD "{{ cookiecutter.project_slug }}" "/src/{{ cookiecutter.project_slug }}"
ADD "pyproject.toml" "/src/pyproject.toml"
ADD "manage.py" "/src/manage.py"
ADD "README.md" "/src/README.md"
ADD "LICENSE" "/src/LICENSE"
WORKDIR /src
RUN python3 -m pip install poetry && python3 -m poetry install
RUN poetry run {{ cookiecutter.project_slug }}-ctl collectstatic --noinput
ENTRYPOINT /bin/sh -c "poetry run {{ cookiecutter.project_slug }}-ctl migrate && poetry run {{ cookiecutter.project_slug }}-ctl server"

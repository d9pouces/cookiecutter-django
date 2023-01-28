"""Define the Django App configuration."""
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class {{ cookiecutter.project_slug|replace("_", " ")|title|replace(" ", "") }}Config(AppConfig):
    """App configuration."""

    default_auto_field = "django.db.models.BigAutoField"
    verbose_name = _("{{ cookiecutter.project_slug }}")
    name = "{{ cookiecutter.project_slug }}"

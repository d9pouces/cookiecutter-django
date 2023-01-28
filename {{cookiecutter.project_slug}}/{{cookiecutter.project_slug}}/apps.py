from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig


class {{ cookiecutter.project_slug|capitalize }}Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    verbose_name = _("{{ cookiecutter.project_slug }}")
    name = "{{ cookiecutter.project_slug }}"

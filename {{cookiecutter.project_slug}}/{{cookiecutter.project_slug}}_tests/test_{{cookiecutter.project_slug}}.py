"""Tests for `{{ cookiecutter.project_slug }}` package."""

{% if cookiecutter.use_pytest == 'y' %}
import pytest
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_content():
    """Sample pytest test function with the pytest fixture as an argument."""
    assert 0 == User.objects.all().count()
{% else %}
from django.contrib.auth.models import User
from django.test import TestCase


class Test{{ cookiecutter.project_slug|replace("_", " ")|title|replace(" ", "") }}(TestCase):
    """Tests for `{{ cookiecutter.project_slug }}` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""
        self.assertEqual(0, User.objects.all().count())
{% endif %}

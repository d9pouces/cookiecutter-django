"""Allow to use python3 -m {{ cookiecutter.project_slug }}."""

from df_config.manage import manage, set_env


def main():
    """Execute the Django management script."""
    set_env("{{ cookiecutter.project_slug }}")
    manage()


if __name__ == "__main__":
    main()

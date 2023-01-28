"""Launch the Django management script with good settings."""
import os
import pathlib

from df_config.manage import manage, set_env


def main():
    """Execute the Django management script."""
    env_path = pathlib.Path("./tools/compose.env")
    if env_path.exists():
        for line in open(env_path):
            if line.startswith("#"):
                continue
            key, sep, value = line.strip().partition("=")
            os.environ[key] = value
    set_env("{{ cookiecutter.project_slug }}")
    manage()


if __name__ == "__main__":
    main()

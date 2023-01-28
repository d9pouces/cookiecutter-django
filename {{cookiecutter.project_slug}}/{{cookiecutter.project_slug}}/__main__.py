"""Allow to use python3 -m {{ cookiecutter.project_slug }}."""
import pathlib

from df_config.manage import manage, set_env


def main():
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

#!/usr/bin/env python3
import os
import pathlib

from df_config.manage import manage, set_env

env_path = pathlib.Path("./tools/compose.env")
if __name__ == "__main__":
    if env_path.exists():
        for line in open(env_path):
            if line.startswith("#"):
                continue
            key, sep, value = line.strip().partition("=")
            os.environ[key] = value
    set_env("{{ cookiecutter.project_slug }}")
    manage()

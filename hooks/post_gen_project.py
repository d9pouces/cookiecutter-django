import subprocess
github_username = "{{ cookiecutter.github_username }}"
project_name = "{{ cookiecutter.project_slug }}"
try:
    subprocess.check_output(["git", "init"])
    if github_username:
        branch = f"git@github.com:{github_username}/{project_name}.git"
        subprocess.check_output(["git", "remote", "add", "origin", branch])
except subprocess.CalledProcessError:
    pass

try:
    subprocess.check_call(["pre-commit", "install"])
    # subprocess.check_call(["pre-commit", "autoupdate"])
except subprocess.CalledProcessError:
    print("WARNING: Unable to install pre-commit ( https://pre-commit.com/ )")

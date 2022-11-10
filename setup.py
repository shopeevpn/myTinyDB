#!/usr/bin/python3
"""
script creates the directories required,
installs required packages
and sets-up a virtual environment
"""

import subprocess
from modules.handle_files import create_dir
from modules.handle_files import generate_key

packages = ["cryptography", "pyperclip", "tinydb==4.5.2"]


def prepare_env(packages: list):
    """
    sets up everything for the user
    Args::
        package(str): the pipenv package
    """
    create_dir()
    generate_key()
    for package in packages:
        subprocess.check_call(["pip3", "install", package])


if __name__ == "__main__":

    prepare_env(packages=packages)

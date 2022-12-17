#!/usr/bin/python3
"""
script creates the directories required,
installs required packages
"""

import subprocess
from modules.handle_files import create_dir
from modules.handle_files import generate_key


def prepare_env():
    """
    sets up everything for the user
    """
    create_dir()
    generate_key()
    subprocess.check_call(["pip3", "install", "-r", "requirements.txt"])


if __name__ == "__main__":

    prepare_env()

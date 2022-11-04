#!/usr/bin/python3
"""
script creates the directories required
and installs required packages
"""
import os
import subprocess
from modules.handle_files import create_dir
from modules.handle_files import generate_key

package = "pipenv"


def prepare_env(package: str):
    """
    sets up everything for the user
    Args::
        package(str): the pipenv package
    """
    create_dir()
    generate_key()
    subprocess.check_call(
            ["pip", "install", package]
            if os.name == "nt"
            else ["pip3", "install", package]
            )

    # installs the packages from the PipFile
    subprocess.check_call(["pipenv install"])

    # activates the virtual envirnonment
    subprocess.check_call(["pipenv shell"])
    print("="*17)
    print("Everything is set")


if __name__ == "__main__":

    prepare_env(package=package)

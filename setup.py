#!/usr/bin/python3
"""
script creates the directories required
and installs required packages
"""
import os
import subprocess
from modules.handle_files import create_dir
from modules.handle_files import generate_key

packages = ["tinydb==4.5.2", "pyperclip"]


def prepare_env(packages: list):
    """
    sets up everything for the user
    """
    create_dir()
    generate_key()
    for package in packages:
        subprocess.check_call(
                ["pip", "install", package]
                if os.name == "nt"
                else ["pip3", "install", package]
            )
    print("="*17)
    print("Everything is set")


if __name__ == "__main__":

    prepare_env(packages)

#!/usr/bin/python3
"""
script creates the directories required
and installs required packages
"""
import os
import subprocess
from modules.handle_files import create_dir

package_name = "tinydb==4.5.2"


def prepare_env(package):
    """
    sets up everything for the user
    """
    create_dir()
    subprocess.run(
            ["pip", "install", package]
            if os.name == "nt"
            else ["pip3", "install", package]
            )
    print("="*17)
    print("Everything is set")


if __name__ == "__main__":

    prepare_env(package_name)

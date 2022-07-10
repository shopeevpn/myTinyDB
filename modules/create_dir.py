#!/usr/bin/python3
"""creates dir where the json file will be"""
import os
from pathlib import Path


class CreateDir:
    def __init__(self) -> None:
        """initialize create dir class"""
        self.home_dir_path = Path.home()

    def change_to_home_dir(self):
        """
        changes to home directory of the os
        """
        os.chdir(self.home_dir_path)
        print("changed to home")

    def create_dir_in_home(self):
        """
        creates 'hidden' directory in the home dir
        """
        CreateDir.change_to_home_dir
        os.mkdir("really_long_directory_name")
        print("done")

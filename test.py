#!/usr/bin/python3

from modules.handle_files import enrcypt_db as crypt
from modules.database import full_path

if __name__ == "__main__":
    crypt(full_path)

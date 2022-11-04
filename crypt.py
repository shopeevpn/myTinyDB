#!/usr/bin/env python3

from modules.database import full_path
from modules.handle_files import encrypt_file, to_key

if __name__ == "__main__":
    encrypt_file(db_path=full_path, key_path=to_key)

#!/usr/bin/python3

from modules.handle_files import encrypt_file, decrypt_file, generate_key, to_key
from modules.database import full_path

if __name__ == "__main__":
    #    generate_key()
#        encrypt_file(db_path=full_path, key_path=to_key)
    decrypt_file(db_path=full_path, key_path=to_key)

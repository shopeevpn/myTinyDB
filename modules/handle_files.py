#!/usr/bin/python3
"""
Module creates a directory in the systems home directory,
"""
import os
from pathlib import Path
from cryptography import fernet as fnt

home_path = Path.home()
dir_name = ".mydb"
to_dir_path = os.path.join(home_path, dir_name)
to_key = os.path.join(to_dir_path, "mydb.key")


def change_to_home():
    """changes directory to the system's home path"""
    os.chdir(home_path)


def create_dir():
    """
    calls change_to_home function
    then creates  directory in the home dir
    """
    change_to_home()
    os.mkdir(dir_name)

def enrcypt_db(db):
    print(db)
    def encrypt_file(db):
        crypt_key = fnt.Fernet.generate_key()
        
        with open(to_key, 'wb') as f_key:
            f_key.write(crypt_key)

        fernet = fnt.Fernet(crypt_key)

        with open(db, 'rb') as db_file:
            original_file = db_file.read()

        encrypted_file = fernet.encrypt(original_file)

        with open(db, 'wb') as file:
            file.write(encrypted_file)

        return fernet

    def decrypt_file(encrypted_file, crypt, key):
        dec_content = crypt.decrypt(encrypted_file)
        with open(db, 'wb') as dec_file:
            dec_file.write(dec_content)

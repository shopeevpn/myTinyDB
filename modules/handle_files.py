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


def generate_key():
    """
    generates the key to be used to encrypt files
    """
    crypt_key = fnt.Fernet.generate_key()
    with open(to_key, 'wb') as f_key:
        f_key.write(crypt_key)


def encrypt_file(db_path: str, key_path: str):
    """
    encrypts the password file

    Args::
        db_path: path to the file
        key_path: path to the generated key
    """

    if os.stat(db_path).st_size == 0:
        print("File is empty skipping encryption") 
    else:
        with open(key_path, 'rb') as key:
            crypt_key = key.read()

        fernet = fnt.Fernet(crypt_key)

        with open(db_path, 'rb') as db_file:
            original_file = db_file.read()

        encrypted_file = fernet.encrypt(original_file)

        with open(db_path, 'wb') as file:
            file.write(encrypted_file)


def decrypt_file(db_path: str, key_path: str):
    """
    decrypts the passwords file

    Args::
        db_path: path to the file location
        key_path: path to the generated key

    """
    with open(key_path, 'rb') as file:
        decrypt_key = file.read()
    
    fer = fnt.Fernet(decrypt_key)
    
    if os.stat(db_path).st_size == 0:
        print("File empty skipping decryption")
    else:
        with open(db_path, 'rb') as file:
            encrypted_file = file.read()

        dec_content = fer.decrypt(encrypted_file)
        with open(db_path, 'wb') as dec_file:
            dec_file.write(dec_content)

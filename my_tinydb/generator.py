#!/usr/bin/python3
"""module generates random passwords"""
import random
import string
import pyperclip


def generate_password():
    """
    generates random values and joins them
    """

    str_source = string.ascii_letters + string.digits + string.punctuation

    generated_string = "".join(random.sample(str_source, 15))
    pyperclip.copy(generated_string)
    print("password copied to clipboard")
    print("*"*28)

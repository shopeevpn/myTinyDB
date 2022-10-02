#!/usr/bin/python3
"""module generates random passwords"""
import random
import pyperclip


class PasswordGenerator():
    """
    defines PasswordGenerator
    """
    def __init__(self) -> None:
        """initialize the generator"""
        self.upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.lower = self.upper.lower()
        self.digits = "0123456789"
        self.symbols = "*&%$#@!+~:-<|?/ >"
        self.empty_string = "" + self.upper

    def start_join(self):
        """
        generates random values and joins them
        """

        self.empty_string += self.digits
        self.empty_string += self.lower
        self.empty_string += self.symbols
        self.password_length = 15

        self.generated_password = "".join(random.sample(
            self.empty_string, self.password_length
            ))
        print()
        print("password copied to clipboard")
        print("*"*28)
        print()
        pyperclip.copy(self.generated_password)


start_generator = PasswordGenerator()

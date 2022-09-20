#!/usr/bin/python3
"""module generates random passwords"""
import random


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

    def take_input(self):
        """take user input"""
        self.password_length = int(input("Length of password: "))
        self.password_amount = int(input("Number of passwords: "))
        if not isinstance(self.password_length, int):
            raise TypeError(f"{self.password_length} has to be an integer")
        elif not isinstance(self.password_amount, int):
            raise TypeError(f"{self.password_amount} has to be an integer")
        elif self.password_amount < 0 or self.password_length < 0:
            raise ValueError("Input needs to be >= 0")
        print()

    def start_join(self):
        """generates random vlues and joins them"""
        print("""
***********************************

        Password generator 

***********************************
    """)
        PasswordGenerator.take_input(self)
        self.empty_string += self.digits
        self.empty_string += self.lower
        self.empty_string += self.symbols

        print("\n", "*"*len(self.upper), "\n")
        for _ in range(self.password_amount):
            self.generated_password = "".join(random.sample(
                self.empty_string, self.password_length
                ))
            print(f"~# {self.generated_password}")


start_generator = PasswordGenerator()

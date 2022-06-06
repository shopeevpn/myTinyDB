import random
import time

def password_generator():
    print("""
****************************************

           Password generator

                yes: y
                no: n

****************************************
    """)
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = uppercase.lower()
    digits = "1234567890"
    symbols = " *&%$#@!+~:-<|?/ >"

    password_length = int(input("Length of password: "))
    password_amount = int(input("Number of passwords: "))
    sym = input("Would you like to use symbols?\n~# ")
    lower = input("Would you like to use lowercase letters?\n~# ")
    nums = input("Would you like to use numbers?\n~# ")
    print()

    # use of symbols
    if (sym == "y"):
        syms = True
    else:
        syms = False

    # use of lowercase letters
    if(lower == "y"):
        lower = True
    else:
        lower = False

    # use of numbers
    if(nums == "y"):
        nums = True
    else:
        nums = False

    # uses uppercase letters no matter what
    upper = True

    
    # empty string where the random values are joined to
    empty_pass = ""

    if upper:
        empty_pass += uppercase

    if lower:
        empty_pass += lowercase

    if nums:
        empty_pass += digits

    if syms:
        empty_pass += symbols

    print("**"*password_length)         
    for _ in range(password_amount):
        generated_password = "".join(random.sample(empty_pass, password_length))
        print(f"~# {generated_password}")


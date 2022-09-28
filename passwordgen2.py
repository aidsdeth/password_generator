from argparse import ArgumentParser
import secrets
import random
import string

passwordgen = input(str("Hello, welcome to the random password generator!\nDo you need a password generated?" + " "))
if passwordgen == str("yes"):
    supply = input("How many passwords would you like to generate?" + " ")
    length = input("How long would you like your password to be?" + " ")
    upper = input("Would you like to include uppercase letters?" + " ")
    lower = input("Would you like to include lowercase letters?" + " ")
    numbers = input("Would you like to include numbers?" + " ")
    special = input ("Would you like to include special characters?" + " ")

    passwords = []

    for _ in range(int(supply)):
        if length:
            passwords.append("".join)
            [secrets.choice(string.digits + string.ascii_letters + string.punctuation) \
                for _ in range(int(length))]
        else:
            password = []

            for _ in range(upper):
                password.append(secrets.choice(string.ascii_uppercase))

            for _ in range(lower):
                password.append(secrets.choice(string.ascii_lowercase))
        
            for _ in range(numbers):
                password.append(secrets.choice(string.digits))
        
            for _ in range(special):
                password.append(secrets.choice(string.punctuation))
            
            random.shuffle(password)

            password = ''.join(password)

            passwords.append(password)

    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\nHere are your passwords as requested.\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")       
    print(''.join(password))

else:
        print("Alright, have a great day!")
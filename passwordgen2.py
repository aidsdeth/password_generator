import secrets
import random
import string

passwordgen = input(str("Hello, welcome to the random password generator!\nDo you need a password generated?" + "(n/Y):" + " "))
if passwordgen == str("Y"):
    supply = input("How many passwords would you like to generate?" + "(#):" + " ")
    length = input("How long would you like your password to be?" + "(#):" + " ")
    upper = input("Would you like to include uppercase letters?" + "(n/Y):" + " ")
    lower = input("Would you like to include lowercase letters?" + "(n/Y):" + " ")
    numbers = input("Would you like to include numbers?" + "(n/y):" + " ")
    special = input ("Would you like to include special characters?" + "(n/y):" + " ")
    output = input("Where would you like to store the passwords?" + "(.txt):" + " ")

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
    if output:
        with open (output, 'w') as f:
            f.write('\n'.join(passwords))

    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\nHere are your passwords as requested.\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print(''.join(password))

else:
        print("Alright, have a great day!")
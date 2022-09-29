import secrets
import string

passwordgen = input(str("Hello, welcome to the random password generator!\nDo you need a password generated?" + "(n/Y):" + " "))
if passwordgen == str("Y"):
    supply = int(input("How many passwords would you like to generate?(#): "))
    length = int(input("How long would you like your password to be?(#): "))
    numbers = input("Would you like to include numbers?(n/Y): ")
    special = input ("Would you like to include special characters?(n/Y): ")
    output = input("Where would you like to store the passwords?(.txt): ")


    passwords = []

    if numbers == str("Y") and special == str("Y"):
        for _ in range(supply):
            passwords.append("".join(
                [secrets.choice(string.digits + string.ascii_letters + string.punctuation) \
                    for _ in range(length)]))

    else:
        if numbers == str("Y") and special == str("n"):
            for _ in range(supply):
                passwords.append("".join(
                    [secrets.choice(string.ascii_letters + string.digits) \
                        for _ in range(length)]))

        else:
            if numbers == str("n") and special == str("n"):
                for _ in range(supply):
                    passwords.append("".join(
                        [secrets.choice(string.ascii_letters) \
                            for _ in range(length)]))

            else:
                if numbers == str("n") and special == str("Y"):
                    for _ in range(supply):
                        passwords.append("".join(
                            [secrets.choice(string.ascii_letters + string.punctuation) \
                                for _ in range(length)]))




    if output:
        with open (output, 'w') as f:
            print("\n".join(passwords), file=f)

    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\nHere are your passwords as requested.\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("\n".join(passwords))

else:
        print("Alright, have a great day!")
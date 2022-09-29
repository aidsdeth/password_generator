import secrets
import string

#adding variable to decide if user would like to generate passwords, and creating condition to continue the program so long user inputs "Y"
passwordgen = input(str("Hello, welcome to the random password generator!\nDo you need a password generated?" + "(n/Y):" + " "))
if passwordgen == str("Y"):
    #Variable to define how many passwords the user would like to generate
    supply = int(input("How many passwords would you like to generate?(#): ")) #Variable to define how many passwords the user would like to generate
    #Variable to define how long each password should be
    length = int(input("How long would you like your password to be?(#): "))
    #Variable that will allow digits in the password generation
    numbers = input("Would you like to include numbers?(n/Y): ")
    #Variable that will allow special characters in the password generation
    special = input ("Would you like to include special characters?(n/Y): ")
    #Variable to define which file to edit or create and store the generated passwords
    output = input("Where would you like to store the passwords?(.txt): ")

    #Variable that defines the list of passwords
    passwords = []

    #Conditional statement that will generate passwords that will INCLUDE digits AND special chars
    if numbers == str("Y") and special == str("Y"):
        for _ in range(supply):
            passwords.append("".join(
                [secrets.choice(string.digits + string.ascii_letters + string.punctuation) \
                    for _ in range(length)]))

    #Conditional statement that will generate passwords that will INCLUDE digits but will NOT INCLUDE special chars
    else:
        if numbers == str("Y") and special == str("n"):
            for _ in range(supply):
                passwords.append("".join(
                    [secrets.choice(string.ascii_letters + string.digits) \
                        for _ in range(length)]))

        #Conditional statement that will generate passwords that will NOT INCLUDE digits and special chars
        else:
            if numbers == str("n") and special == str("n"):
                for _ in range(supply):
                    passwords.append("".join(
                        [secrets.choice(string.ascii_letters) \
                            for _ in range(length)]))

            #Conditional statement that will generate passwords that will NOT INCLUDE digits but will INCLUDE special chars
            else:
                if numbers == str("n") and special == str("Y"):
                    for _ in range(supply):
                        passwords.append("".join(
                            [secrets.choice(string.ascii_letters + string.punctuation) \
                                for _ in range(length)]))


    #This condition will print generated passwords to a created or editted file
    if output:
        with open (output, 'w') as f:
            print("\n".join(passwords), file=f)

    #This print value is always printed when program is finished running
    print("Here are your passwords as requested!")
    print("\n".join(passwords))

#This condition stops the whole process if the user inputs ANYTHING BUT "Y" to the first question
else:
        print("Alright, have a great day!")
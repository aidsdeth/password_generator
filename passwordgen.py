from argparse import ArgumentParser
import secrets
import random
import string

parser = ArgumentParser(
  prog="Random Password Generator",
  description="For when you need to generate a randomized password.")

#Adding argument to define length of password
parser.add_argument("-p", "--password-length", default=8, type=int, help="Define the desired length of your generated password.")
#Adding argument to define the supply or number of passwords
parser.add_argument("-s", "--supply", default=1, type=int, help="Define how many passwords you would like to generate.")
#Adding argument to define where the user wants to store the passwords
parser.add_argument("-o", "--output-file", help="Define where the passwords will be stored.")

args = parser.parse_args()

passwords = []
#Generates list of passwords
for _ in range(args.supply):
  #Generates passoword based on defined length
  if args.password_length:
    passwords.append("".join(
      [secrets.choice(string.digits + string.ascii_letters + string.punctuation) \
        for _ in range(args.password_length)]))
  else:
    password = []
    #Shuffle password
    random.shuffle(password)
    #Joins all generated characters together
    password = ''.join(password)
    #Appends current password to list of passwords
    passwords.append(password)

if args.output_file:
  with open(args.output_file, 'w') as i:
    i.write('\n'.join(passwords))


print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\nHere are your passwords as requested.\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print('\n'.join(passwords))

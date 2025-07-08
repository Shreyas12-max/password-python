# Password generator and Verifier
# Created by Shreyas
# Created Date : 7th July 2025

import random
import string

print ("Welcome to password creator and verifier")

Length = int(input("Enter password Length :"))

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation
all_chars = letters + digits + symbols

password = " "
for i in range(Length):
    password += random.choice(all_chars)

print("Your generated password is :" , password)

entered = input("Enter the password")
confirm = input("Confirm the password")

if entered == password and confirm == password:
    print("Password matched and fixed")

else:
    print("Entered wrong password")










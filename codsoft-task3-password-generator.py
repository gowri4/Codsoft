#PASSWORD GENERATOR

#import library from python
import random
import string

#User input
length = int(input("Enter the Length of your PASSWORD: "))

#Declaring password characters
chars = string.ascii_letters
chars += string.digits
chars += string.punctuation

#generating the new passsword
generate_password = ""

for i in range(length):
    password_characters = random.choice(chars)
    generate_password += password_characters
    
#result is displayed
print("Your generator_password is: \n", generate_password)
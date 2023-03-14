import math
import random
import pyperclip

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
passwords_generated = 0

def handle_generation():
    global passwords_generated
    global alphabet

    length_input = input("Enter the length you want your password to be:\n")
    while(length_input==""):
        length_input = input("Enter the length you want your password to be:\n")

    prefix_input = input("Enter the prefix you want to use for your password:\n")
    while(prefix_input == ""):
        prefix_input = input("Enter the prefix you want to use for your password:\n")

    password = prefix_input

    for i in range(int(length_input)):
        random_password_int = math.floor(random.random()*10)
        random_alphabet_index = math.floor(random.random()*30)
        random_letter_chance, random_uppercase_chance = random.random(), random.random()

        if random_alphabet_index >= 25: random_alphabet_index = math.floor(random.random()*21)
        
        if random_letter_chance > 0.5:
            letter = alphabet[random_alphabet_index]
            if random_uppercase_chance > 0.5:
                password += letter.upper()
            else:
                password += letter.lower()
        else:
            password += str(random_password_int)

    passwords_generated = passwords_generated + 1

    print("The generated password has been copied to your clipboard")
    pyperclip.copy(password)

    return password

while True:
    print(handle_generation())
    print(passwords_generated)

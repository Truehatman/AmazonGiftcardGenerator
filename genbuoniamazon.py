import random
import string
import time
import sys

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

num_strings = 1
string_length = 16

while True:
    print("\nMenu:")
    print("1. Generate Amazon Giftcard")
    print("2. End Software")

    user_choice = input("Chose the number: ")

    if user_choice == "1":
        num_strings = int(input("How many giftcard do you want to generate: "))
        print('Generating giftcard...')
        time.sleep(5)

        print("\nAmazon Giftcard Generated:\n")
        for i in range(num_strings):
            new_string = generate_random_string(string_length)
            print(new_string)
            time.sleep(3)

        print("All Giftcard Generated successfully")
        
    elif user_choice == "2":
        print("Generator terminated.")
        break

    else:
        print("Command don't exist")

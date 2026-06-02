import time
import itertools
import string

def brute_force(target_password, max_length=6):
    chars = string.ascii_lowercase + string.digits
    attempts = 0

    print(f"Cracking the password : {'*' * len(target_password)}")
    print("Starting brute force.....\n")

    for length in range(1, max_length+1):
        for guess in itertools.product(chars, repeat=length):
            attempts += 1
            guess_password = ''.join(guess)
            if guess_password == target_password:
                print(f"Password found: {guess_password}")
                print(f"Total attemtps: {attempts}")
                return guess_password
    
    print("Password not found. Try again.")

brute_force("abc123")

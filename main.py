import itertools
import string
import time


# Goes through a list of common passwords
def guess_common_passwords(password):
    with open('common_passwords.text', 'r') as passwords:
        data = passwords.read().splitlines()
    # print(data)

    for i, match in enumerate(data):
        if match == password:
            return f'The password is: {match} (Attempt #{i})'

    return 0


# Goes through every combination of chars
def brute_force(password, min_length=3, max_length=16):
    # Modify this for total symbols
    chars = string.ascii_lowercase + string.digits
    attempts = 0
    for password_length in range(min_length, max_length):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == password:
                return f'password is {guess}. found in {attempts} guesses.'
            print(guess, attempts)


# Tries the common passwords first, then uses the brute force function
def get_password(password):
    common = guess_common_passwords(password)
    return brute_force(password) if common == 0 else common


# Get the current timestamp
start_time = time.time()

# Find the password
print(get_password('vale'))
# Print the time it took
print(round(time.time() - start_time, 2), 's')

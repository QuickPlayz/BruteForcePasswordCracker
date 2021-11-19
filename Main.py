import itertools
import string
import time

I = input('Whats your password')

def guess_password(real):
    chars = string.ascii_lowercase + string.digits + string.ascii_uppercase
    attempts = 0
    startTime = time.time()
    for password_length in range(1, 9):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == real:
                endTime = time.time()
                elapsedtime = endTime - startTime
                return 'password is {}. found in {} guesses. took {} seconds to crack'.format(guess, attempts, elapsedtime)

print(guess_password(I))

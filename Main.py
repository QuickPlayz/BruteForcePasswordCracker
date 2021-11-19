import itertools
import string
import time

print('Made by @Quickplayz on Github')
print('---------------------------')
I = input('Whats your password')
print('---------------------------')


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
                average = attempts / elapsedtime
                return 'password {}. {} guesses. took {} seconds. average is {} guesses per second'.format(guess, attempts, elapsedtime, average)
print(guess_password(I))

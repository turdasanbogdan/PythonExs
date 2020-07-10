from random import randint, sample
from string import ascii_letters, digits, punctuation
def pass_generator(x):
    s = ascii_letters+digits+punctuation
    password = sample(s, x)
    password = "".join(password)
    return password
print(pass_generator(int(input("How many caract in your pass? "))))
print(ascii_letters)
print(digits)
print(punctuation)
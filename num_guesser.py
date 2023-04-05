import string
import random

print("Welcome to password generator pgm")

alpha = string.ascii_letters
"""string.ascii_lower & ascii_upper"""
digit = string.digits
special = string.punctuation

colle = alpha + digit + special

plen = int(input("length of password: "))

r = int("random.sample("colle,plen")"):

print(r)

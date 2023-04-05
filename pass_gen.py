# WsCube Tech: generate random password
import random
import string

print("welcome to password generator! ")

def function():


    pwdlen = int(input("password lenght:" ))

    letter = string.ascii_letters
    number = string.digits
    char = string.punctuation
    
    comb = (letter + number + char)
    ra = random.sample(comb, pwdlen)
    """sample is use to return new value on every run"""
    password = "".join(ra)
    """join method is used to convert list value into string"""

    print(password)
    function()
function()    
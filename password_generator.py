# learn with Tim

import random
import string

def generate_password(min_length, numbers=True, special_character=True):
    le = string.ascii_letters
    dig = string.digits
    special = string.punctuation

#     print(le, dig, special)

# generate_password(10)

    character = le  
    """ letters, numbers, special character all are store at one place i.e. in character"""
    if numbers:
       character += dig
    if special_character:
       character += special

    
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
       new_char = random.choice(character)
       """generating random number from character and storing it into new_char"""
       pwd += new_char 
       """random values in new_char are store in pwd"""

       if new_char in dig :
            #   """if values in new_char belongs to dig then has_number is true"""
              has_number = True
       elif new_char in special:
            #   """if values in new_char belongs to special then has_char is true"""
              has_special = True

  
    meets_criteria = True
    if numbers:
            meets_criteria = has_number
    if special_character:
            meets_criteria =  meets_criteria and has_special
    # return pwd

    pwd = generate_password(10)
    print(pwd)

           
          

              









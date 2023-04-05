#wscode, count the vowel in sentence

sen = input("Enter your sentence: ") 
"""we can also put .lower() here"""
vowel = ['a', 'e', 'i', 'o', 'u']
count = 0
for char in sen.lower():
    if char in vowel:
        count = count+1
      
print(count)        
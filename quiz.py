print("welcome to my Computer Quiz!")

start = input("Do you want to play? ")

if start.lower() != "yes":
    quit()

print("Okay! Let's start :)")   
score = 0 

Question =input("What does cpu stands for? ").lower()
if Question == "central processing unit":
    print("correct!")
    score = score + 1
else:
    print("incorrect")
    

Question =input("What does Ram stands for? ")
if Question.lower() == "random access memory":
    print("correct!")
    score = score + 1
else:
    print("incorrect")

    
Question =input("What does gpu stands for? ").lower()
if Question == "graphic processing unit":
    print("correct!")
    score = score + 1
else:
    print("incorrect")
 

Question =input("What does Rom stands for? ").lower()
if Question == "Read only memory":
    print("correct!")
    score = score + 1
else:
    print("incorrect")
   

Question =input("What does BCD stands for? ").lower()
if Question == "Binary coded decimal":
    print("correct!")
    score = score + 1
else:
    print("incorrect")
    

print("you got " + str(score) + " question correct")    
print("you got " + str((score/5)*100) + "%")







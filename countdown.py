
import time 

print("WELCOME TO COUNTDOWN")
t = int(input("Enter the length of the countdown in sec: "))

#for x in reversed(range(0, t)):

 
for x in range(t, 0, -1):
 seconds = x % 60
 minus = int(x/60)%60

 hrs = int(x/3600)%60
 print(f"{hrs:02}:{minus:02}:{seconds:02}")

    
    #print(x)
    
 time.sleep(1)
print("Time is up!!")
   





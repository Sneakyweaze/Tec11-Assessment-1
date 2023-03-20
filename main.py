#this is the list for the questions.
Question = ["How Many Gyms are there in the school? ","What class block is the science block? ","What is the name of the area between B Block, The hall and the admin building? ",]
#this list is all the answers for the questions.
Answer  = ["3","F Block","A Quad",]
#this is the varible for what question/answer is
qanum = 0 
#this is the varible for how many point you have 
points = 0
#this imports time and says hello ; then waits o.5 seconds 
import time
print("Hello User")
time.sleep(0.5)
#asks user for name, saves as username 
username = input("What is your Name? ")
#say that the quiz is starting, prosent question[qanum]
while qanum <= 4:
 userasr = input(Question[qanum])
 if userasr == Answer[qanum]:
    print("You're Correct!")
    points += 1
    qanum += 1
    if qanum == 3: 
     break
    else:
     continue
 else:
   print("That Is Incorrect, the answer was",Answer[qanum],"!")
   qanum += 1
   if qanum == 3: 
     break
   else:
    continue

print("hello")
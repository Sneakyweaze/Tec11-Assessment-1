#this is the list for the questions.
Question = ["How Many Gyms are there in the school? ","What class block is the science block? ","What is the name of the area between B Block, The hall and the admin building? ","Where is The Tennis Corts? ","What subject is studied in G Block? ","What do you learn in K block? ","What do you learn in M block? ","What block do you learn Social Studies? ","What do you learn in A block? ","What is the class number for referral? "]
#this list is all the answers for the questions.
Answer  = ["three","f block","a quad","behind gym one","english","languages","music","d block","art","f eleven"]
#this is the varible for what question/answer is
qanum = 0 
#this is the varible for if the loop is on or not
loop = "yes"
#this is the function that says somtheing is correct
def yes_function():
  print("That Is Correct!")
#this is the function that says somtheing is incorrect
def no_function():
  print("That Is Incorrect!")
#this is the varible for how many point you have 
points = 0
#this function removes trailing .0 from percentages
def formatNumber(dec2):
  if dec2 % 1 == 0:
    return int(dec2)
  else:
    return dec2

import time
#this is where the code will be reset if the user wants to play again
while loop == "yes":
#says hello and then waits o.5 seconds 
 print("Hello User")
 time.sleep(0.5)
#asks user for name, saves as username 
 username = input("What is your Name? ")
 time.sleep(0.5) 
 print("Please Use A Lowercase Letter At The Start Of Each Word and don't use numbers in your answers")
 time.sleep(0.5)
#say that the quiz is starting, prosent question[qanum]
 while qanum != len(Answer) + 1:
  userasr = input(Question[qanum])
  if userasr == Answer[qanum]:
    yes_function()
    points += 1
    qanum += 1
    if qanum == len(Answer): 
     break
    else:
     continue
  else:
   no_function()
   qanum += 1
   if qanum == len(Answer): 
     break
   else:
    continue

# when out of questions, the code will show score and ask to play again.
 print("You Have Finshed The Quiz.")
 time.sleep(0.5)
 print(username,",You Got ",points,"out of",len(Question),"Questions Correct.")
 dec1 = points / len(Answer)
 dec2 = dec1 * 100
 time.sleep(0.5)
 print("Thats a",formatNumber(dec2),"% success rate ")
 time.sleep(0.5)
 loop = input("do you want to play again? ")
 if loop == "yes":
  qanum = 0
  time.sleep(0.5)
  print("resetting...")
  time.sleep(0.5)
  print("            ")
  time.sleep(0.5)
  continue 
 else:
  time.sleep(0.5)
  print("good bye")

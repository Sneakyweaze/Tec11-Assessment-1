#this adds OS, which is used to clear the console when to code resets
import os
#This is the list for the questions.
Question = ["How Many Gyms are there in the school? ","What class block is the science block? ","What is the name of the area between B Block, The hall and the admin building? ","Where are The Tennis Courts? ","What subject is studied in G Block? ","What do you learn in K block? ","What do you learn in M block? ","What block do you learn Social Studies? ","What do you learn in A block? ","What is the class number for referral? "]
#This list is all the answers for the questions.
Answer  = ["three","f block","a quad","behind gym one","english","languages","music","d block","art","f eleven"]
#this is the variable for what question/answer is
qanumber = 0 
#this is the variable for if the loop is on or not
loop = "yes"
#this is the function that says something is correct
def yes_function():
  print("That Is Correct!")
#this is the function that says something is incorrect
def no_function():
  print("That Is Incorrect!")
#this is the variable for how many point you have 
points = 0
#this function removes trailing .0 from the percentage of success rate
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
 print("\n")
#asks user for name, saves as username: states the rules of the quiz 
 username = input("What is your Name? ")
 time.sleep(0.5) 
 print("\n")
 print("Please Use A Lowercase Letter At The Start Of Each Word and don't use numbers in your answers")
 time.sleep(0.5)
#say that the quiz is starting, prosent question[qanumber]
 while qanumber != len(Answer) + 1:
  print("\n")
  time.sleep(0.5)
  userasr = input(Question[qanumber])
#if question is correct,the code adds one to points and qanumber: continues loop
  if userasr.lower() == Answer[qanumber]:
    print("\n")
    time.sleep(0.5)
    yes_function()
    points += 1
    qanumber += 1
    if qanumber == len(Answer): 
     break
     time.sleep(0.5)
    else:
     continue
#if question is incorrect,the code doesn't adds one to points and adds one to qanumber: continues loop
  else:
   print("\n")
   time.sleep(0.5)
   no_function()
   qanumber += 1
   if qanumber == len(Answer): 
     break
     time.sleep(0.5)
   else:
    continue

# When out of questions, the code will show score and success rate and ask to play again.
 print("You Have Finished The Quiz.")
 time.sleep(0.5)
 print("\n")
# this shows how many points the user got out of how many questions there are
 print(username,",You Got ",points,"out of",len(Question),"Questions Correct.")
 dec1 = points / len(Answer)
 dec2 = dec1 * 100
 time.sleep(0.5)
 print("\n")
# this shows the percentage of what questions the user correct to incorrect
 print("Thats a",formatNumber(dec2),"% success rate ")
 time.sleep(0.5)
 print("\n")
 loop = input("do you want to play again? ")
#if the user responds with yes, the code will reset.
 if loop == "yes":
  qanumber = 0
  points = 0
  time.sleep(0.5)
  print("\n")
  print("resetting...")
  time.sleep(1)
# this clears the console
  os.system('clear')
  time.sleep(0.5)
  continue 
#if the user responds with something that isn't yes, the code will end.
 else:
  time.sleep(0.5)
  print("\n")
  print("good bye")
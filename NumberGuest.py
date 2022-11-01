# Guessing game like live!

import random
import time

print("Hi Welcome to the guessing game. I am going to pick a number between 1 and 100.")

print("Picking number...")

time.sleep(3)

guess = int(input("What is your guess number between 1,100?: "))

correct_ans = random.randint(1,10)

guess_count = 1

while guess != correct_ans:
  guess_count+=1
  if guess < correct_ans:
    guess = int(input("Try again guess higher. What is your guess?: ")) 
  else:
    guess = int(input("Try again guess lower. What is your guess?: ")) 
    
print(f"Boo!You got the right answer.It took you {guess_count} guesses.")

#Sureyya Betul Akis26
#creates a menu-driven program that allows a user to enter five numbers (integers)

def main():
  firstInput  = 0
  secondInput = 0
  thirdInput  = 0
  fourtInput  = 0
  fifthInput  = 0

  while True:
    firstInput  = AcceptUsersInput()
    secondInput = AcceptUsersInput()
    thirdInput  = AcceptUsersInput()
    fourtInput  = AcceptUsersInput()
    fifthInput  = AcceptUsersInput()
    userList    = [firstInput, secondInput, thirdInput, fourtInput, fifthInput]
    menu_driven()
    answer = int(input(" Enter your answer: "))
    if answer == 1:
      theSmallest(userList)
    elif answer == 2:
      theLargest(userList)
    elif answer == 3:
      theSumof5(userList)
    elif answer == 4:
      theAverage(userList)
    else:
      break
    
def AcceptUsersInput():
  Input  = int(input("Enter a numbers between 25 to 225  (integers):"))
  while(not(Input >= 25 and Input <= 225)):
    print("Error, please try again!")
    Input  = int(input("Enter a numbers between 25 to 225  (integers):"))
  return Input

def menu_driven():
  print(" _______\n")
  print("  MENU")  
  print(" _______\n")
  print(" 1.  Find the Smallest number")
  print(" 2.  Find the Largest number")
  print(" 3.  Find the Sum of numbers")
  print(" 4.  Find the Average of numbers") 
  print(" 5.  End\n")

def theSmallest(userList):
  print(min(userList))

def theLargest(userList):
  print(max(userList))

def theSumof5(userList):
  print(sum(userList))

def theAverage(userList):
  print(float(sum(userList)) / max(len(userList),1))
  
main()

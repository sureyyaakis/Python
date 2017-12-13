# Sureyya Betul AKIS
# Extra Assignment: COMP 1411 calculating grade

def main():
    while True:
      quiz = AcceptUsersInput_quizes()
      programming_assignment_1 = AcceptUsersInput_programming_assignment_1()
      programming_assignment_2 = AcceptUsersInput_programming_assignment_2()
      programming_assignment_3 = AcceptUsersInput_programming_assignment_3()
      programming_assignment_4 = AcceptUsersInput_programming_assignment_4()
      programming_assignment_5 = AcceptUsersInput_programming_assignment_5()
      programming_assignment = [programming_assignment_1, programming_assignment_2, programming_assignment_3,programming_assignment_4, programming_assignment_5]

      lab_1 = AcceptUsersInput_labs_1()
      lab_2 = AcceptUsersInput_labs_2()
      labs = [lab_1, lab_2]

      midterm = AcceptUsersInput_midterm()
      wish_grade = AcceptUsersInput_wish_grade()
      quiz_and_assignment = (quiz_dropped_lowest_average(quiz) + programming_assignment_average(programming_assignment))/2
      midterm_x2 = midterm * 2
 
      lab_last_average = lab_average(lab_1, lab_2)
      print("=" * 55)
      print('Current quiz average after dropping lowest score is:', quiz_dropped_lowest_average(quiz), '%')
      print("Current programming assignment average is:", programming_assignment_average(programming_assignment),'%')
      print('Current labs average is:', lab_average(lab_1, lab_2),'%')
      print('Currently, the grade score for the course is:',current_grade(quiz_and_assignment,lab_last_average,midterm_x2),'%')
      print('The student will get', full_onFinal(quiz, programming_assignment,lab_1, lab_2, midterm_x2), 'out of 100 if the student receives 100% on final.')
      print('To receive the anticipated grade the student should receive', should_receive_on_final(quiz, programming_assignment,lab_1, lab_2, midterm_x2),'%', ' on final exam, which means the student should receive', 'out_of_75()', 'out of 75 to get an', wish_grade, 'grade')
      
      answer = input("Do you want to re-enter all the scores for another student?")
      if answer == 'yes':
          return main()
      else:
        break


def AcceptUsersInput_quizes():
  quizes = [int(x) for x in input("Please enter quiz scores as a list(5 valid scores):").split()]
  for a in quizes:  # quiz value control
      if ((a < 0) or (a > 10) or (len(quizes) < 5) or (len(quizes) > 5)):
          print("Error, please try again!")
          return AcceptUsersInput_quizes()

  return quizes

def AcceptUsersInput_programming_assignment_1():
  programming_assignment_1 = int(input("Please enter score for programming assignment 1:"))
  while (not (programming_assignment_1 >= 0 and programming_assignment_1 <= 50)):
    print("Error, please try again!")
    programming_assignment_1 = int(input("Please enter score for programming assignment 1:"))
  return programming_assignment_1


def AcceptUsersInput_programming_assignment_2():
  programming_assignment_2 = int(input("Please enter score for programming assignment 2:"))
  while (not (programming_assignment_2 >= 0 and programming_assignment_2 <= 75)):
    print("Error, please try again!")
    programming_assignment_2 = int(input("Please enter score for programming assignment 2:"))
  return programming_assignment_2


def AcceptUsersInput_programming_assignment_3():
  programming_assignment_3 = int(input("Please enter score for programming assignment 3:"))
  while (not (programming_assignment_3 >= 0 and programming_assignment_3 <= 100)):
    print("Error, please try again!")
    programming_assignment_3 = int(input("Please enter score for programming assignment 3:"))
  return programming_assignment_3


def AcceptUsersInput_programming_assignment_4():
  programming_assignment_4 = int(input("Please enter score for programming assignment 4:"))
  while (not (programming_assignment_4 >= 0 and programming_assignment_4 <= 125)):
    print("Error, please try again!")
    programming_assignment_4 = int(input("Please enter score for programming assignment 4:"))
  return programming_assignment_4


def AcceptUsersInput_programming_assignment_5():
  programming_assignment_5 = int(input("Please enter score for programming assignment 5:"))
  while (not (programming_assignment_5 >= 0 and programming_assignment_5 <= 150)):
    print("Error, please try again!")
    programming_assignment_5 = int(input("Please enter score for programming assignment 5:"))
  return programming_assignment_5


def AcceptUsersInput_labs_1():
  labs_1 = int(input("Please enter score for lab 1:"))
  while (not (labs_1 <= 125)):
    print("Error, please try again!")
    labs_1 = int(input("Please enter score for lab 1:"))
  return labs_1

def AcceptUsersInput_labs_2():
  labs_2 = int(input("Please enter score for lab 2:"))
  while (not (labs_2 <= 150)):
    print("Error, please try again!")
    labs_2 = int(input("Please enter score for lab 2:"))
  return labs_2

def AcceptUsersInput_midterm ():
  midterm = int(input("Please enter score for midterm:"))
  while midterm > 50 or midterm < 0:
    print("Error, please try again!")
    midterm = int(input("Please enter score for midterm:"))
  return midterm

def AcceptUsersInput_wish_grade():
  wish = input("What grade do you wish to receive? ")
  while (not (wish == 'A' or wish == 'B' or wish == 'C')):
    print("Error, please try again!")
    wish = input("What grade do you wish to receive? ")
  return wish

def quiz_dropped_lowest_average(quiz):
  return ((sum(quiz) - min(quiz)) *10) // (max(len(quiz),1) - 1)

def programming_assignment_average(programming_assignment):
  return (sum(programming_assignment)) // max(len(programming_assignment), 1)

def lab_average(lab_1, lab_2):
  return int(((lab_1 + lab_2) / (125+150)) * 100)

def current_grade(quiz_and_assignment,lab_last_average,midterm_x2):
  a_g_per = (quiz_and_assignment/100)*20 
  lab_per = (lab_last_average / 100)*20
  midterm_per =(midterm_x2/100)*30
  per_sub = a_g_per + lab_per + midterm_per
  last = (per_sub * 100)/70
  return "%.2f" % last
 
def full_onFinal(quiz, programming_assignment,lab_1, lab_2, midterm_x2):
  assigment_quiz_p = ((((quiz_dropped_lowest_average(quiz) + programming_assignment_average(programming_assignment))/ 2)/100)*20)
  lab_p = (lab_average(lab_1,lab_2) / 100) *20
  midterm_p = (midterm_x2 / 100* 30)
  final = 100
  final_p = (final / 100) *30
  return assigment_quiz_p + lab_p + midterm_p + final_p
  
def should_receive_on_final(quiz, programming_assignment,lab_1, lab_2, midterm_x2):
  different = 96 - full_onFinal(quiz, programming_assignment,lab_1, lab_2, midterm_x2)
  final_grade_guess = 30 + different
  guess_percent = (final_grade_guess * 100)/30
  return "%.2f" % guess_percent
  
def out_of_75():
  a = (should_receive_on_final *75)/100
  return a
  
 
main()



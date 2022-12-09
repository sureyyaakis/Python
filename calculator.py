# define the function
def calculator(num1, operator, num2):
  if operator == '+':
    return num1 + num2
  elif operator == '-':
    return num1 - num2
  elif operator == '*':
    return num1 * num2
  elif operator == '/':
    return num1 / num2

# take input from the user
num1 = float(input('Enter a number: '))
operator = input('Enter an operator (+, -, *, /): ')
num2 = float(input('Enter another number: '))

# call the function and print the result
result = calculator(num1, operator, num2)
print(result)

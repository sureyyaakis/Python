def bark():
  print("Woof woof!")

#100 times calls the func
for x in range(100):
  bark()

#Any name we can add it will call
def hello(name):
  print(f"Hello {name}")

hello("Sara")

def add_numbers(num1,num2):
  print(num1+num2)

add_numbers(4,8)

#--------

def dog_info(age,name):
  print(f"Dog age {age}, and Dog name is {name}")

dog_info(2,"Popi")

def double(number):
  return number * 2

new_number = double(5)

print(new_number)

#--------
def uppercase(text):
  return text.upper()

print(uppercase("mary"))

names = ["nick", "Jane", "sara"]

for name in names:
  print(uppercase(name))

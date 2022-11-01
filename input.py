user_name = input("What is your name? ")
print(f"Hello {user_name}")

user_number = int(input("What do you want to double? "))
print(user_number * 2)

#---upper lower case ex

user_text= input("Enter some text: ")

upper_or_lower = input("Enter 1 to uppercase and 2 to lowercase: ")

if upper_or_lower=="1":
  print(user_text.upper())
else: 
  print(user_text.lower())
  

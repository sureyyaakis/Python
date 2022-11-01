import random 

lucky_num = random.randint(1,100)

fortune_cookie = random.randint(1,3)

fortune_text = ''

if fortune_cookie == 1:
  fortune_text = 'You will have a great day!'
elif fortune_cookie == 2:
  fortune_text = 'Today will be tough...but worth it!'
else:
  fortune_text = "Don't give up!"
print(f'{fortune_text} Your lucky number is: {lucky_num}')

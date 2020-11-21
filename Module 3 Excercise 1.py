# Module 3 Excercise 1

import random #bring in radom function
target_num, guess_num = random.randint(1, 10), 0 #set range
while target_num != guess_num: #set logic
    guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
print('You guessed right!')
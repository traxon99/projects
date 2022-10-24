'''
Author: Jackson Yanek
KUID: 3094054
Date: 09/23/2022
Lab: lab03
Last modified: 09/23/2022
Purpose: word guesser
'''
password = 'bringcoffee'
correct = False

print('Guess the secret phrase!')
guess_count = 0
while correct == False:
    guess_count = guess_count + 1
    guess = input('Guess: ')
    if len(guess) > len(password):
        print('Too many characters')
    if len(guess) < len(password):
        print('Too few characters')
    if len(guess) == len(password):
        if guess == password:
            print('Correct!')
            print('Number of guesses:', guess_count)
            break
        else: 
            counter = 0
            index = 0
            for letter in password:
                if guess.upper()[index] == letter.upper():
                    counter += 1
                index +=1
            print('Correct letters:',counter)

'''
Author: Jackson Yanek
KUID: 3094054
Date: 09/16/2022
Lab: lab02
Last modified: 09/16/2022
Purpose: Divide sodas into different packaging.
'''


soda = int(input('How many sodas do you have? '))

cubes = soda // 24
left_over1 = soda % 24
six_packs = left_over1 // 6
remaining = left_over1 % 6

print(f'Fridge Cubes: {cubes}')
print(f'Six-packs: {six_packs}')
print(f'Singles: {remaining}')

'''
Author: Jackson Yanek
KUID: 3094054
Date: 09/16/2022
Lab: lab02
Last modified: 09/16/2022
Purpose: Long division printer
'''

num = int(input('Enter a numerator: '))
denom = int(input('Enter a denominator: '))

if denom == 0:
	print('Sorry, you may not divide by zero.')
	print('Exiting...')
else:
	ans = num // denom
	rmdr = num % denom
	print(num,"/",denom,"=",ans,"Remainder",rmdr)
	print('Exiting...')

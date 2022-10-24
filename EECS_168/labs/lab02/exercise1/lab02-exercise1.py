'''
Author: Jackson Yanek
KUID: 3094054
Date: 09/16/2022
Lab: lab02
Last modified: 09/16/2022
Purpose: Categorizes hurricanes based on user input of wind speed.
'''
w_s = int(input('Input a wind speed (m/s):')) ##w_s is wind speed input value

if 0 <= w_s < 18:
	print('A wind speed of',w_s,'is a tropical depression.') 

elif 18 <= w_s < 33:
	print('A wind speed of',w_s,'is a Tropical Storm.')

elif 33 <= w_s < 43:
	print('A wind speed of',w_s,'is a Category 1 hurricane.')

elif 43 <= w_s < 50:
	print('A wind speed of',w_s,'is a Category 2 hurricane.')

elif 50 <= w_s < 58:
	print('A wind speed of',w_s,'is a Category 3 hurricane.')

elif 58 <= w_s < 70:
	print('A wind speed of',w_s,'is a Category 4 hurricane.')

elif 70 <= w_s:
	print('A wind speed of',w_s,'is a Category 5 hurricane.')

elif w_s < 0:
	print('Invalid wind speed')

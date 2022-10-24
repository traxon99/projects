'''
Author: Jackson Yanek
KUID: 3094054
Date: 09/23/2022
Lab: lab03
Last modified: 09/23/2022
Purpose: infection calculator
'''
temp = 0
infected = [1,4,64]

print('Outbreak!')
desired_day = int(input('What day do you want a sick count for? (integer) '))
if desired_day > 0:
    if desired_day < 4:
        print('Total people with the flu:',infected[desired_day - 1])
    elif desired_day == 4:
        print('Total people with the flu: 69')
    elif desired_day > 4:
        day = 3 # day - 1 is index for 

        while day <= desired_day:
            temp = sum(infected[day - 3: ])
            infected.append(temp)
            day += 1
        print('Total people with the flu:',infected[desired_day - 1])
else:
    print('Invalid day.')

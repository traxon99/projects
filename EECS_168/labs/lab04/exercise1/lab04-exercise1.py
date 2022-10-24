'''
Author: Jackson Yanek
KUID: 3094054
Date: 09/30/2022
Lab: lab04
Last modified: 09/30/2022
Purpose: Going to the Grocery Store 
'''


items = []
while True:
    choice = 0
    print('\nWelcome to your Shopping List \n1)Add item\n2)Check off item\n3)Print List\n4)Exit')
    choice = int(input('Enter a choice:'))
    if choice == 1:
        add = input('What would you like to add to your list? ')
        items.append(add.strip())
    elif choice == 2:
        check_off = items[int(input('What item would you like to check off? '))-1]
        for item in items:
            if item == check_off:
                items[items.index(check_off)] = item[0]+((len(item)-2)*'-')+item[len(item)-1]
    elif choice == 3:
        print('\nHere is your list: ')
        for i in range(len(items)):
            print(str(i+1)+')',items[i])
    elif choice == 4:
         print('Goodbye!')
         break

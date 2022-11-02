'''
Author: Jackson Yanek
KUID: 3094054
Date: 10/21/2022
Lab: lab06
Last modified: 10/26/2022
Purpose: Function Lab 
'''

def last_digit(num):
    num = str(num)
    new_num = num[-1]
    return new_num

def remove_last_digit(num):
    if len(num) > 1:
        new_num = num[0:-2]
        return new_num
    else:
        return '0'

def add_digit(current_num, new_digit):
    new_num = str(current_num) + str(new_digit)
    return new_num

def reverse(num):
    new_num = last_digit(num)
    for i in range(len(str(num))):
        if i > 1:
            new_num = add_digit(new_num,int(str(num)[-i]))
    new_num = str(new_num) + str(num)[0]
        
    'new_num = str(num)[::-1]'
    return new_num

def is_palendrome(num):
    if str(num) == reverse(num):
        return True
    else:
        return False

def count_digits(num):
    return len(str(num))

def sum_digits(num):
    num = str(num)
    sum = 0
    for digit in num:
        sum = sum + int(digit)
    return str(sum)

def print_menu():
    print('1) Count digits\n2) Sum digits\n3) Is palendrome\n4) Reverse\n5) Exit\n Choice:')

def main():
    while True:
        print_menu()
        choice = input()
        if choice == '1':
            num = int(input('Choose num: '))
            print(count_digits(num))
        elif choice == '2':
            num = int(input('Choose num: '))
            print(sum_digits(num))
        elif choice == '3':
            num = int(input('Choose num: '))
            print('Palendrome:',is_palendrome(num))
        elif choice == '4':
            num = int(input('Choose num: '))
            print(reverse(num))
        elif choice == '5':
            break
        else:
            print('Invalid input')


main()
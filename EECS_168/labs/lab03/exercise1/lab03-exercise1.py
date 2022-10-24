'''
Author: Jackson Yanek
KUID: 3094054
Date: 09/23/2022
Lab: lab03
Last modified: 09/23/2022
Purpose: sequence search
'''

stringinput = input('Enter a string: ')
case_sens = input('Do you want a case-sensitive match: (y/n) ')


if case_sens.upper() == 'Y':
    seq = input('Enter a sequence to count: ')
    print('In the string', stringinput, 'the sequence', seq, 'occurs', stringinput.count(seq),'time(s)')
if case_sens.upper() == 'N':
    seq = input('Enter a sequence to count: ')
    print('In the string', stringinput, 'the sequence', seq, 'occurs', stringinput.upper().count(seq.upper()),'time(s)')


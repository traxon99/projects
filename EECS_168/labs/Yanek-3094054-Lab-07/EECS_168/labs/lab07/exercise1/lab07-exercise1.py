'''
Author: Jackson Yanek
KUID: 3094054
Date: 10/31/2022
Lab: lab07
Last modified: 11/02/2022
Purpose: File Handling Lab
'''

def clean_word(word):
    exclusions = ['!', '?', ':', ';', ',', '|', '.', '[', ']','(',')','--']
    ucw = word.lower()
    for exclusion in exclusions:
        if exclusion == '--':
            ucw = ucw.replace(exclusion,' ')
        else: 
            ucw = ucw.replace(exclusion,'')
    return ucw


def build_count(file):
    words = {}
    opened_file = open(file, 'r')
    for line in opened_file:
        line = line.replace('\n','')
        line = line.split(' ')
        for word in line:
            word = clean_word(word).strip()
            if word in words:
                words[word] = words[word] + 1
            else: 
                words[word] = 1
    return words

def unique_words_fcn(dict):
    unique = []
    for key in dict.keys():
        if dict[key] == 1:
            unique.append(key)
    return unique



def main():
    word = "Welcome to Jackson's word counter!" 
    print(word.center(60,'='))
    file_name = input('Enter a file name: ')
    words = build_count(file_name)
    print(f'The file {file_name} has been processed.')
    print(f'The output has been stored in word_data.txt and unique_words.txt.')
   
    word_data = open('word_data.txt','w')
    for key in words.keys():
        word_data.write(f'{key}: {words[key]}\n')
    
    unique_words = open('unique_words.txt','w')
    unique_words.write(f'Here is a list of unique words in {file_name}:\n')
    for word in unique_words_fcn(words):
        unique_words.write(f'{word}\n')
    print('Exiting...')
main()

'''
Author: Jackson Yanek
KUID: 3094054
Date: 09/30/2022
Lab: lab05
Last modified: 10/19/2022
Purpose: Web History Simulator 
'''


def main():
    curr_hist_index = 0
    history = []

    while True:
        usr_cmd = input('Enter a command:')


        usr_cmd = usr_cmd.split(' ')
        if len(usr_cmd) > 1:
            website = usr_cmd[1]
            usr_cmd = usr_cmd[0]
        else: 
            usr_cmd = usr_cmd[0]
        

        if usr_cmd == 'NAVIGATE':
            if len(history) == 0:
                
                history.append(website)
                curr_hist_index = history.index(website)
                            
            elif curr_hist_index + 1 != (len(history)):
                for x in (range(len(history) - curr_hist_index - 1)):
                    history.pop()
                
                history.append(website)
                curr_hist_index = history.index(website)
            
            else:
                
                history.append(website)
                curr_hist_index = history.index(website)
                
        
        elif usr_cmd == 'BACK':
            if curr_hist_index != 0:
                curr_hist_index -= 1
        
        
        elif usr_cmd == 'FORWARD':
            if curr_hist_index != (len(history) - 1):
                curr_hist_index += 1
        
        
        elif usr_cmd == 'HISTORY':
            print('Oldest')
            print('=========')
            for site in history:
                if history.index(site) == curr_hist_index:
                    print(site,'<=====')
                else:    
                    print(site)
            print('=========')
            print('Newest')
        
        
        if usr_cmd == 'EXIT':
            break

main()
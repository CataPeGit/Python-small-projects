""" countdown timer """

import time

#time is in seconds for this code

def countdown(t):   
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end = "\r")
        print('\r')
        time.sleep(1)
        t -= 1
    print("Timer completed!")

t = input('Enter the time in seconds: ')

countdown(int(t))
        

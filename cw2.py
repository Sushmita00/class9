'''import from cw1
print(cw1.name)
print(cw1.age)
print(cw1.place)



from cw1 import name,age
import cw1
age=23
print(name)
print(age)

from cw1 import *
print(name)
print(age)
print(place)

#date and time
'''
import datetime as dt
import time
print(dt.date.today())
print("Formatted Time: ", time.asctime())



#web  Browser
import webbrowser
a=input("searching video")
print("open Browser")
webbrowser.open_new_tab('http://youtub.com/search?q=%s'%a)


#os library
import os
print('my current working directory:',os.getcwd())


#math library
import math
num=(int(input("enter a number:")))
print("factorial:",math.factorial(num))
#add colour in terminal

from termcolor import colored
print(colored('hello','red','on_rey'),colored('world','green','on_red'))
text=colored('Color look nice!!!','blue',attrs=['reverse','blink'])
print(text)



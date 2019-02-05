#using the OS library change the name of a file.

import os
print("my current working directory is : ",os.getcwd())
print("class 10",os)



#using print the current weekday,week,month and year in separate statement.

import datetime as dt

print(dt.date.today())
today = dt.date.today()
print(" year :",today.year)
print(" month:",today.month)
print(" day:",today.day)

#use two function from the math library.


import math
num=int(input("enter the value of num:"))
#print(math.sqrt(num))
print("sqrt:",math.sqrt(num))



import math
num=int(input("enter the value of num:"))
#print(math.log10(num))
print("log10:",math.log10(num))



#find more interesting library

import peewee

db=peewee.sqlitedatabase('my_app.db')
class Book(peewee.model):
      author=peewee.CharField()
      title=peewee.TextField()

      class Meta:
            database=db

if __name__== '__main__':

   db.contact()
   Book.create_table(True)

   book = Book.filter(author='Gabor Laszlo Hajba',title='python 3 in Anger' )
   book.save()
   for book in Book.filter(author='Gabor Laszlo Hajba'):
         print("book title")
   db.close()


import matplotlib.pyplot as plt
x_axis=[x for x in range(-3,4)]
y_axis=[x*x for x  in x_axis]

plt.plot(x_axis,y_axis)
plt.show()


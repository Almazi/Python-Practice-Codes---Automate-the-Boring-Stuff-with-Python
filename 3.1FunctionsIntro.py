#Third party module
import pyperclip as pclip #this module is handy to copy pase text on clipboard
name = input("What is your name? ")
pclip.copy(name)
print ("we will paste your name three times using pyperclip module's copy paste functions: ", pclip.paste()*3)


#standard modules like random sys etc
import random
randomlyChosen = random.randint(-5,10)
print("Using .accesor, randomly chosen between two integer:", randomlyChosen)

from random import * #improting all the functions of random module
randomlyChosen = randint(-5,10)
print("Using fromr random import *, randomly chosen between two integer:", randomlyChosen)

from random import randint as rint #only improting the randint function as a variable named rint
randomlyChosen = rint(1,10)
print("Using from random import randint as rint, randomly chosen between two integer:", randomlyChosen)

import sys #system functions

stop = 7
while  randomlyChosen != 7:
    print("Randomly chosen number is: ",randomlyChosen,"We didnt choose 7 yet, Again choose!")
    randomlyChosen = rint(1,10)
else:
    print("We found a 7 as randomly chosen number! the program will exit using sys.exit() function :D ")
    sys.exit()

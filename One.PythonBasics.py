#Using print function where I am sending the arguments what I want to print
print("Hello wooorld!")

print("What is your name?")
#Using the input function where it will take input from my input device and save in the myName variable
myName = input()
print("Length of your name is: ")
#the len function will determine the length of myName string
print(len(myName))
print("How are you?",myName)
myStatus = input()

print("Is it AM or PM time now?")
timeStatus = input()
if timeStatus == 'AM':
    print("Whats the time in AM now?")
    #Concerting the format from string to integer and saving to time
    time = int(input())
else:
    print("Whats the time in PM now?")
    time = int(input())
print("So in 24hours format the time will be: ")
if timeStatus == "PM" :
    time = 12 + time
else:
    time = time
print(time)
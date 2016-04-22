print("Loooooop")

inputString = int(input("Give me a number, any number, I will iterate that many times: "))
while inputString > 0:
    print("Iterate step: ",inputString)
    inputString -= 1
name = input("Please enter your name: ")
while name == '':
    name = input("You didnt enter anything as your name, please do it: ")
else:
    print("Thank you for entering your name: ",name)
    option = int(input("If you would like to change the entery please press 1, or just press 0 if you are done"))
    if option == 1 :
        name = input("Please enter your name: ")
        while name == '':
            name = input("You didnt enter anything as your name, please do it: ")
        else:
            print("Thank you for entering your name: ",name)
            option = int(input("If you would like to change the entery please press 1, or just press 0 if you are done"))
    elif option == 0:
        print("Final input of your name: ",name)


for variable in range(5):
    print(variable)

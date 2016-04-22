print("And statements: ")
print("True and True: ",True and True)
print("True and False:",True and False)
print("False and True: ",False and True)
print("False and False: ",False and False)
print("OR statements: ")
print("True or True: ",True or True)
print("True or False:",True or False)
print("False or True: ",False or True)
print("False or False: ",False or False)
name = input("Whats your name: ")
if name == "bob":
    print("hello bob!")
else:
    print("You are not bob, you are:",name,"dame you!")
age = int(input("Whats your age?: "))
if age <= 10:
    print("You are a kid",name)
elif age > 10 and age <20:
    print("Yo ar a teenager",name)
elif age >= 20 :
    print("here comes the pressure of world")
else:
    print("You are nothing")
print("Bool checker")
print("Blank input is 0 or False in bool: ")
bool(' ')

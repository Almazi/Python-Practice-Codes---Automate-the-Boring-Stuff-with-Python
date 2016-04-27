#Variables declared in any particular function/method is local scope as it is usable only locally. Same named variable used in globally can be used in local too
def localstuff():
    global variable #It will determine the "variable" as global no matter what you declare in local scope, it will always use global one
    variable = "Local variable"
    print(variable)

variable = "Global variable"
localstuff() #Though we locally declared varaible, still it will print global variable
print(variable)

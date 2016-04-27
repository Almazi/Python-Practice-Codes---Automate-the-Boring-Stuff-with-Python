def divideByAnything(dividend, divisor):
    try:
        result = dividend / divisor
        print("The result is: ",result)
    except:
        print("You must put a number! please try again: ")
        dividend = int(input("Input the number you want to divide: "))
        divisor = int(input("Input the number you want to divide by: "))
        divideByAnything(dividend, divisor)

dividend = int(input("Input the number you want to divide: "))
divisor = int(input("Input the number you want to divide by: "))
divideByAnything(dividend, divisor)


try:
	#Exception can be raised from anywhere even in Try block. we create an instance of the NameError exception
	raise NameError('Exception') #Pay close attention to how we raise a NameError exception while passing in the string "Exception".
except NameError:		#catch that instance
	print "Our raised exception was caught"

try:
	print 1 / 0
except:
	print "Something bad happened"
finally: #When dealing with exceptions,we might want to have something happen regardless of an error that gets raised. This can be accomplished by using a finally statement. The "finally" block will execute no matter what happens
	print "This will always be executed"

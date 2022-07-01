
try:
    #everything attempted under the try 
    #will be attempted until there's an error! 
    num = input("Type in number:\n>")

    num = int(num)

    print (100 / num)

except ValueError:
    print("You typed something in that isn't a number!")

except ZeroDivisionError:
    print("You can't divide by zero!")    

except Exception as problem:
    #if it fails, try this instead1
    print("RUH ROH RAGGY.", problem) 

else:
    print("I only run if there were no errors!")    

finally:
    print("i always run, error or not")    
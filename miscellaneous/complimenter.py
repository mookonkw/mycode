#keyword arguments
def complimenter1(x,y="awesome"):
    print(f"{x} is {y}!")

complimenter1(y= "mabel" , x="a rockstar")    

#positional arguments
def slappy(first, second):
    print(first)
    print(second)

slappy("abc", "123")    

#require a certain TYPE of object as an argument
#does not work because you cannot define by type??
#  def addition(x :int):
#    print(x + 100)

#  addition(str("abc")) 

def complimenter2(x: "str"):
     # type checking
        #if type(x)
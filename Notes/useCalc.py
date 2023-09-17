#You can import one module into another using the import keyword
#import calc  #You can import all the names from the module into the current namespace.
#from calc import multi, sub #You can import just a particular name or collection of names from a module.
import calc as cl #You can rename module after importing it.
import math 

print(cl._add(10,10))
#print(multi(3,6)) # This statement is valid only if you used "from calc import multi"
print(math.ceil(4.5))

'''
Runtime error does not appear until after the program has started running. These errors are also called exceptions because they usually indicate that something exceptional (and bad) has happened.
Exceptions are handled using try/except/finally mechanism.
''' 
while True:
    try:
        x = int(input("Enter a number "))
        print(cl._add(2,x))
        break
    except ValueError:
        print("Enter a valid number")




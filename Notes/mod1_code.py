
int_1  = 3345465 #int
float_1 = 3.4    #float
bool_1 = True    #bool
##############################
#Collections
#set
set_1 = set()
set_2 = {1,2,3,4,'a'}
#Dict
dict_1 = dict()
dict_2 = {'a':1, 'b':'bb'}
#print(dict_2['a'])
#str
str_1 = ''
str_2 = "CSE2050"
#print(str_2[4] , str_2[0])
#list
list_1 = []
list_2 = [1,2,5, 7, 'abc', [7,8,9]]
#print(list_2)
#Tuples
tup_1 = tuple() #or ()
tup_2 = (2,3,4,'a', (3,4,5))
###################################
#Operations on collections 
#- Iterating over a collection
for key,values in dict_2.items():
    print(key,values)
for ele in tup_2:
    print("Tuples" , ele)

#- Sequence slice
#[start:end]
list_3 = ["John", "Ava", "Bill", "Nancy"]
'''
print(list_3[0:3])
print(list_3[:2])
print(list_3[1:])
print("The last element :", list_3[-1])
print("last 3 elements : ", list_3[-3:])
print(list_3[1:-1])
'''

#Length
print(len(list_3))

#####################################
#if statement : The ability to check conditions and change the behavior of the program accordingly.
x = 4
y = 4
if x > y : 
    print(str(x)+ " is greater than "+ str(y) )
elif x == y: 
    print(str(x)+ " is equal to "+ str(y) )
else:
    print(str(x)+ " is less than "+ str(y) )

#Range : The range type represents an immutable sequence of integer numbers and is commonly used for looping a specific number of times in for loops.
#range(start, stop, step)
#range(stop)
#range(start,stop)
list_5 = []
for w in range(0,4,2):
    list_5.append(w)
print(list_5)
list_6 = []
for r in range(11):
    list_6.append(r)
print(list_6)

######################
#Functions :A Function is a block of code that only runs when it called
# - Function arguments can have a default value assigned in the function definition.

def addition(x,y=10):
    print("Addition" ,x+y)


addition(3,5) 
addition(10)
addition(3)
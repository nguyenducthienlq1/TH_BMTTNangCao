a = 8
b = 4
print(a , "+", b  ," = " , a + b)
print(a , "-", b  ," = " , a - b)
print(a , "*", b  ," = " , a * b)
print(a , "/", b  ," = " , a / b)
print(a , "%", b  ," = " , a % b)
print(a , "^^", b  ," = " , a**b)
print("-------------------------")
name = "Alice"
age = 8
isValid = True
if isValid:
    {
        print("Name: ", name),
        print("Age: ", age)
    }
print("-------------------------")
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)
print(a == b)
print(a != b)
print(a > b or a >= b)
print(a > b and a >= b)
print("-------------------------")
fruits = ["apple", "banana","aloalo"]
for fruit in fruits:
    print(fruit)
count = 0
while count < 5:
    print(count)
    count += 1
print("-------------------------")
singlequote = 'avsdasfsd'
doublequote = "asdsdfgdfsgsdafsaf"
triplequote = '''asfasdfsdfsdaf
dsfasdfsdfasdf
sdfasdfasdfsdaf'''
mystring = "Hello World"
print(mystring[6:])
def my_func(a, b):
    return a + b
print("tong 2 so la: ", my_func(a,b))
print("-------------------------")
from array import array
int_array = array('i',[1,2,3,4,5,6])
int_array.append(1)
for element in int_array:
    print(element)

my_tuple = (1,2,3,4,5,1,1,1)
print(my_tuple.count(1))
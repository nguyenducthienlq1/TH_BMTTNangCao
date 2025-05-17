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
print("------------------------")
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "Hanoi"
}
print(my_dict["name"])  
print(my_dict["age"])   

my_dict["email"] = "alice@example.com"  
my_dict["age"] = 26  
print(my_dict)

del my_dict["city"] 
print(my_dict)

age = my_dict.pop("age")  
print(age)
print(my_dict)

if "name" in my_dict:
    print("Name exists in the dictionary.")

for key in my_dict:
    print(key)

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(key, value)

print("---------------------------------------")
class Person:
    
    def __init__(self, name, age):
        self.name = name  
        self.age = age    

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


person1 = Person("Alice", 25)
person2 = Person("Bob", 30)


print(person1.name)  
print(person1.age)   
person1.greet()      

#Ke thua
# Lớp cha
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

# Lớp con kế thừa từ lớp Animal
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows")

dog = Dog("Buddy")
dog.speak()  

cat = Cat("Whiskers")
cat.speak()  
#Da hinh
class Bird(Animal):
    def speak(self):
        print(f"{self.name} chirps")

animals = [Dog("Buddy"), Cat("Whiskers"), Bird("Tweety")]

for animal in animals:
    animal.speak()  
#Dong goi
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Thuộc tính private
    
    def deposit(self, amount):
        self.__balance += amount
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")
    
    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.get_balance())  # Output: 1300

#Truu tuong hoa
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")

dog = Dog()
dog.speak()  # Output: Woof!





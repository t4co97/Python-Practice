#Run ptyon
print("Tyler Westbrook")
print("Never gonna give you up")
print("Never gonna let you down")
print("Never gonna run around and desert you")
print("Never gonna make you cry")
print("Never gonna say goodbye")
print("Never gonna tell a lie and hurt you")
print()

#variables
print(1,2,3,4,5)
print(64+32)
x = 7
y = 2
print(x+y)
print()

#Strings
print("Eddie Murphy")
s = "lucky" 
print(s)
print("Today is 3/15/2021")
print()

#String Replace
txt = "abc 123 abc 123"
print(txt)
x = txt.replace("abc","cba",1)
y = txt.replace("123","321",1)
print(x)
print(y)

#String Find
print(txt.find("abc"))
print(txt.find("Abc"))
input1 = input()
print(txt.find(input1))
print()

#String Join
mylist = ["red","blue","green"]
print(mylist)
z = "_".join(mylist)
print(z)
print() 

#String Split
txt1 = "World,Earth,America,Canada"
print(txt1.split(","))
print()

#Random numbers
from random import seed
from random import randint
seed(1)

x = randint(0,10)

print(randint(0,1000000000),randint(0,1000000000),randint(0,1000000000))

randomIntList = []
for x in range(100):
  randomIntList.append(randint(0,10))

for x in range(10):
  print(randomIntList.count(x))

print() 
#Keyboard Input
phone = input("Please enter your phone number:")
lang = input("Please enter your preferred programming language:")
print()

#if statements
input2 = input("Type a number between 1 and 10")
if int(input2) > 10 or int(input2) < 0:
  print("Invalid Number")
else:
  print("Thank You")

password = input("Please enter the password:")
if password == "wasspord":
  print("password correct!")
else:
  ("password incorrect!")
print()

#for loops
clist = ["Canada","USA","Mexico"]
for state in clist:
  print(state)
for x in range(11):
  for y in range(11):
    print(x*y)

for x in reversed(range(11)):
  print(x)
for x in range(101):
  print(x)

for x in range(11):
  if x%2 == 0:
    print(x)  

loop_sum = 0
for x in range(100,200):
  loop_sum+=x
print(loop_sum)
print()

#while loop
i = 0
while i < len(clist):
  print(clist[i])
  i+=1 

while_sum = 0
i=0
while i < 10:
  while_sum+=i
  i+=1
print(while_sum)
i=0
while i < 10:
  for x in range(10):
    i+=1
print

#functions
def sum_list():
  mylist2 = [1,2,3,4,5]
  print(sum(mylist2))
sum_list() 

def call_func():
  sum_list() 
call_func()

def call_itself(k):
  if k > 1:
    print(call_itself(k-1))
  else: 
    print(k+2)
call_itself(3)

def variable_scope():
  variable_scope.scope_variable = 21
  return variable_scope.scope_variable
variable_scope()
def add():
  print(variable_scope.scope_variable)
add()
print

#Lists
states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming" ]
for i in range(len(states)):
  if states[i][0] == 'M':
    print(states[i])
print

#List operations
y = [6,4,2]
y.extend([12,8,4])
print(y)
y[1] = 3
print(y)
print

#Sorting List
def takefirst(elem):
    return elem[0]
x = [ (3,6),(4,7),(5,9),(8,4),(3,1)]
x.sort(key=takefirst)
print(x)

def takeSecond(elem):
    return elem[1]
x = [ (3,6),(4,7),(5,9),(8,4),(3,1)]
x.sort(key=takeSecond)
print(x)
print

#Range Function
my_list = list(range(1, 1001))

print(min(my_list))
print(max(my_list))

odd_list = []
even_list = []
for i in range(len(my_list)):
  if my_list[i] % 2 == 0:
    even_list.append(my_list[i])
  else:
    odd_list.append(my_list[i])
print(even_list)
print(odd_list)
print

#Dictionary
countries = {'United States' : 'USA', 'Germany' : 'GER'}
for i in countries:
  print(i, countries[i])

#Read a file
#f = open("demofile.txt", "r")
#f.read() 
#error message: file not accessible

#Write file
#f.write('take it easy')
#f.write("open(“text.txt”)")

#Nested Loops
for i in range(3):
  for j in range(3):
    print(i,j)
persons = ["John", "Marissa", "Pete", "Dayton"]
for i in range(len(persons)):
  j = i
  while j < len(persons) -1:
    print(f"{persons[i]} meets {persons[j+1]}") 
    j += 1



#Slices
pizzas = ["Hawaii","Pepperoni","Fromaggi","Napolitana","Diavoli"]
print(pizzas[2:4])
string = "hello world"
print(string[6:11])

#Multiple Return
def func1(a,b):
  sum1 = a+b
  list1 = [a,b]
  return list1, sum1

print(func1(1,3))

def five_var(a,b):
  one = a * b
  two = one * 2
  three = one * 3
  four = one * 4
  five = one * 5
  return one,two,three,four,five
print(five_var(5,17))

#Scope
def reduce_balance(balance):
  new_bal = balance - 100
  return new_bal
initial_balance = 1000
new_balance = reduce_balance(initial_balance)

#Time and date
from datetime import date
today = date.today()
print("Today's date:", today)

#Try-except
#Can try-except be used to catch invalid keyboard input?
#yes
#Can try-except catch the error if a file can‟t be opened?
#yes
#When would you not use try-except?
#when dealing with errors, like out of memory 

#Can you have more than one class in a file?
#yes
#Can multiple objects be created from the same class?
#yes
#Can objects create classes?
#no, objects are instances of classes
#Using the code above, create another object?
class Person:
    "This is a person class"

    def get_age(self): 
        return self._age 
      
    def set_age(self, x): 
        self._age = x 
    def greet(self):
        print('WAASSSUUUPPPPP')
    
    def location(self):
      print("Indiana")
Tyler = Person()
Tyler.set_age(21)  
print(Tyler.get_age()) 

#Why would you use getter and setter methods?
#ensures data encapsulation, which avoids direct access to a specific variable 

import math
print(math.sin(6))

def snake():
  print("ssss im a slithery lil snake ")
import main
main.snake()

class Base1:
    pass

class Base2:
    pass

class MultiClass(Base1, Base2):
    pass

#Can a method inside a class be called without creating an object?
#yes - this is called a static method
#Why does not everybody like static methods?
#Static methods have limited use, because they don't have access to the attributes of an instance of a class, and they don't have access to the attributes of the class itself. Its not the best option for long-term use.

#What is an iterable?
#An iteratable is a Python object that can be used as a sequence. You can go to the next item of the sequence using the next() method. It’s a container object: it can only return one of its element at the time. 
#Which types of data can be used with an iterable?
#Examples of iterables include all sequence types (such as list , str , and tuple ) and some non-sequence types like dict , file objects, and objects of any classes you define with an __iter__() method or with a __getitem__() method that implements Sequence semantics

#What is a classmethod?
#A class method is a method that’s shared among all objects. Class methods can be can be called from instances and from the class itself
#How does a classmethod differ from a staticmethod?
#static method is not bound to any one class, while a class method is

#Do all programming languages support multiple inheritance?
#No - one example being java
#Why would you not use multiple inheritance?
#to prevent ambiguity
#Is there a limit to the number of classes you can inherit from?
#no
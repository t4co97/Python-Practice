#Basics
#What is an expression?
#Expressions are representations of value. They are different from statement in the fact that statements do something while expressions are representation of value.

#What is a syntax error?
#Syntax errors are produced by Python when it is translating the source code into byte code. They usually indicate that there is something wrong with the syntax of the program.

#What is PEP8?
#PEP 8, sometimes spelled PEP8 or PEP-8, is a document that provides guidelines and best practices on how to write Python code. ... The primary focus of PEP 8 is to improve the readability and consistency of Python code. PEP stands for Python Enhancement Proposal, and there are several of them.

# What does a linter do?
#lint, or a linter, is a static code analysis tool used to flag programming errors, bugs, stylistic errors, and suspicious constructs. The term originates from a Unix utility that examined C language source code.

#What is the result of this expression: “*” * 10
print("*"*10)#**********

################### What is CPython?#######################
#CPython is the reference implementation of the Python programming language. Written in C and Python, CPython is the default and most widely used implementation of the language.

#How is CPython different from Jython?
#CPython is the original implementation, written in C. (The "C" part in "CPython" refers to the language that was used to write Python interpreter itself.) Jython is the same language (Python), but implemented using Java.

#How is CPython different from IronPython?
#CPython is the original implementation, written in C and IronPython interpreter was written in C#.

#Primitive Types
#1. What is a variable?
#A Python variable is a reserved memory location to store values. In other words, a variable in a python program gives data to the computer for processing

#2. What are the primitive built-in types in Python?
#Python has four primitive types: integers, floats, booleans and strings.

#3. When should we use “”” (tripe quotes) to define strings?
#Spanning strings over multiple lines can be done using python's triple quotes. It is also used for long comments in code. Special characters like TABs, verbatim or NEWLINEs can also be used within the triple quotes

#4. Assuming (name = “John Smith”), what does name[1] return?
name = "John Smith"
print(name[1])#o

#5. What about name[-2]?
print(name[-2])#t

#6. What about name[1:-1]?
print(name[1:-1])#ohn Smit

#7. How to get the length of name?
len(name)

#8. What are the escape sequences in Python?
#\newline Backslash and newline ignored
#\\ Backslash (\)
#\' Single quote (')
#\" Double quote (")
#\a ASCII Bell (BEL)
#\b ASCII Backspace (BS)
#\f ASCII Formfeed (FF)
#\n ASCII Linefeed (LF)
#\r ASCII Carriage Return (CR)
#\t ASCII Horizontal Tab (TAB)
#\v ASCII Vertical Tab (VT)
#\ooo Character with octal value ooo
#\xhh Character with hex value hh

#9. What is the result of f“{2+2}+{10%3}”?
print(f"{2+2}+{10%3}")#4+1

#10. Given (name = “john smith”), what will name.title() return?
name = "john smith"
print(name.title())#John Smith

#11. What does name.strip() do?
#The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)

#12. What will name.find(“Smith”) return?
print(name.find("Smith"))#-1

#13. What will be the value of name after we call name.replace(“j”, “k”)?
print(name.replace("j", "k"))#kohn smith

#14. How can we check to see if name contains “John”?
name.find("John")

#15. What are the 3 types of numbers in Python?
#There are three distinct numeric types: integers, floating point numbers, and complex numbers. In addition, Booleans are a subtype of integers.

#######################Control Flow########################
#1. What is the difference between 10 / 3 and 10 // 3?
print(10/3) #3.3333333333333
print(10//3)#3
#2. What is the result of 10 ** 3?
print (10**3)#1000
#3. Given (x = 1), what will be the value of after we run (x += 2)?
#3

#4. How can we round a number?
x = round(5.76543, 2)
print(x)

#5. What is the result of float(1)?
print(float(1))#1.0

#6. What is the result of bool(“False”)?
print(bool("False"))#true

#7. What are the falsy values in Python?
#Falsy values include empty sequences (lists, tuples, strings, dictionaries, sets), zero in every numeric type, None , and False .

#8. What is the result of 10 == “10”?
print(10=="10")#False

#9. What is the result of “bag” > “apple”?
print("bag">"apple")#true
#10. What is the result of not(True or False)?
print(not(True or False))#False

#11. Under what circumstances does the expression 18 <= age < 65 evaluate to True?
#when age is equal or greater than 18 but less than 65

#12. What does range(1, 10, 2) return?
#1, 3, 5, 7, 9

#13. Name 3 iterable objects in Python.
#Lists, tuples, dictionaries, and sets are all iterable objects

#Functions 
#1. What is the difference between a parameter and an argument? 
#Function parameters are the names listed in the function's definition. Function arguments are the real values passed to the function. Parameters are initialized to the values of the arguments supplied.

#2. All functions in Python by default return …? 
#none
#3. What are keyword arguments and when should we use them? 
#Keyword arguments can often be used to make function calls more explicit. Used when
#We can often leave out arguments that have default values.
#We can rearrange arguments in a way that makes them most readable.
#We call arguments by their names to make it more clear what they represent.

#4. How can we make a parameter of a function optional? 
def f(required_arg, optional_arg1 = "1"):
  print(required_arg, optional_arg1)
f("a")
#5. What happens when we prefix a parameter with an asterisk (*)? 
#Include the *args parameter at the end of a function declaration to allow the user to pass in an arbitrary number of arguments as a tuple.

#6. What about two asterisks (**)? 
#the ** operator allows us to take a dictionary of key-value pairs and unpack it into keyword arguments in a function call.

#7. What is scope? 
#Local (or function) scope is the code block or body of any Python function or lambda expression. This Python scope contains the names that you define inside the function. ... If the local scope is an inner or nested function, then the enclosing scope is the scope of the outer or enclosing function.

#8. What is the difference between local and global variables? 
#Local variable is declared inside a function whereas Global variable is declared outside the function. Local variables are created when the function has started execution and is lost when the function terminates, on the other hand, Global variable is created as execution starts and is lost when the program ends.

#9. Why is using the global statement a bad practice? 
#Global variables are dangerous because they can be simultaneously accessed from multiple sections of a program. This frequently results in bugs.

#Coding Exercises 
#1. Write a function that returns the maximum of two numbers. 
def maximum(k,j):
  print(max(k,j))
  return max(k,j)
maximum(2,3)
#2. Write a function called fizz_buzz that takes a number. 
#1. If the number is divisible by 3, it should return “Fizz”. 
#2. If it is divisible by 5, it should return “Buzz”. 
#3. If it is divisible by both 3 and 5, it should return “FizzBuzz”. 
#4. Otherwise, it should return the same number. 
def fizz_buzz(k):
  if k%3==0 and k%5==0:
    print("FizzBUzz")
    return "FizzBuzz"
  elif k%3==0:
    print("Fizz")
    return "Fizz"
  elif k%5==0:
    print("Buzz")
    return "Buzz"
  else:
    print(k)
    return k
fizz_buzz(10)
fizz_buzz(15)
  
#3. Write a function for checking the speed of drivers. This function should have one parameter:  speed. 
#1. If speed is less than 70, it should print “Ok”. 
#2. Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit  point and print the total number of demerit points. For example, if the speed is 80, it  should print: “Points: 2”. 
#3. If the driver gets more than 12 points, the function should print: “License suspended”
def speed_check(k):
  points = 0
  if k < 70:
    print("ok")
  else:
    while k > 70:
      k-=5
      points+=1
      if k <= 70:
        print(f"Points:{points}")
        break
      elif points > 12:
        print("License suspended")
        break
speed_check(160)
speed_check(90)
#4. Write a function called showNumbers that takes a parameter called limit. It should print all  the numbers between 0 and limit with a label to identify the even and odd numbers. For  example, if the limit is 3, it should print: 
#o 0 EVEN 
#o 1 ODD 
#o 2 EVEN 
#o 3 ODD 
def show_numbers(limit):
  i=0
  while i < limit:
    if i%2==0:
      print(f"{i} Even")
    else:
      print(f"{i} Odd")
    i+=1
show_numbers(10)
#5. Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter).  For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20. 
def multiples(limit):
  i = 0
  multiples_sum = 0
  while i <= limit:
    if i%3==0 or i%5==0:
      multiples_sum+=i
    i+=1
  print(multiples_sum)
multiples(20)

#6. Write a function called show_stars(rows). If rows is 5, it should print the following: o * 
#o ** 
#o *** 
#o **** 
#o ***** 
def show_stars(rows):
  i = 0
  while i <= rows: 
   print(i * "*")
   i+=1
show_stars(7)

#7. Write a function that prints all the prime numbers between 0 and limit where limit is a  parameter.
def prime_numbers(limit):
  i = 2
  j = 0
  for i in range(2,limit):
    for j in range(2,i+1):
      if i==j:
        print(i)
      elif i%j==0:
        break
      j+=1
  i+=1
prime_numbers(20)
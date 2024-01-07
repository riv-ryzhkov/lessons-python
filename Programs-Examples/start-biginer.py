# -------------------------------------------------------------------------------
# Name:        The Complete Python for Beginners
# -------------------------------------------------------------------------------

# THE BEGINNING

"""
Step-1 :
Python installation
https://www.python.org/downloads/

After installation, check whether Python is installed or not.
# >>> open terminal/command prompt
# >>> python3 --version

If the command is executed and Python version is displayed on the screen, then you have
successfully installed Python. If you are getting any error, then just Google it. Python has
a huge community online; you will get many solutions for that error.

"""

"""
Step-2 :
Now we need a text editor to type the Python program. There are many online and offline
editors. If you're a beginner, you can start using Notepad++, Sublime Text Editor, etc.

You can also use Google Colab to run Python programs.

-> https://colab.google/

"""

# Hello World! in Python
print('Hello World!')

# How to run a Python program, follow this link
# https://www.javatpoint.com/how-to-run-python-program


# -------------------------------------------------------------------------------
# TASK 1: Write a Python program to print your college name and school name
# -------------------------------------------------------------------------------

"""
What is Python?
https://www.python.org/doc/essays/blurb/
"""

"""
Decoding this code:
print('Hello World!')

Let's separate this code

1. print
2. 'Hello World!'
3. ()

1. print is a built-in function of Python which will display anything on the screen.
Anything you write inside this function will display as output.

2. Anything enclosed in '' or "", it is called a string. Strings are nothing
but a sequence of characters or a collection of characters.

3. () These are brackets. Here in this snippet, we used brackets to make the code more readable.

Finally, the Hello World! will print on the output screen.

"""
# -------------------------------------------------------------------------------
# TASK 2: Why is Python known as an interpreted programming language
# -------------------------------------------------------------------------------


# PYTHON IDENTIFIERS

"""
Python identifier is the name we give to identify a
varaible , function , class , module , or other object.

Rules for writing identifiers:
    1. Use only alphanumeric characters and underscores.
    2. Never start with a number
    3. Use underscores to separate two words
    4. Keywords cannot be indentifers

    example:
        # valid
        age = 24
        name = "python-guide"

        #invalid
        2name = "java"
        class = helo


Read More:
    https://www.geeksforgeeks.org/python-keywords-and-identifiers/
"""
# -------------------------------------------------------------------------------
# TASK 3: Why the above identifers are invalid (Do reasearch and find the correct answer)
# -------------------------------------------------------------------------------

# PYTHON DATA-TYPES
# https://www.geeksforgeeks.org/python-data-types/
# https://www.w3schools.com/python/python_datatypes.asp

rating = 5
name = "python"
is_pass = True
marks = 77.5

print(type(rating))
print(type(name))
print(type(is_pass))
print(type(marks))
print('=' * 80)
# Note:- In python we have built-in function named type() to check data type of variable

# -------------------------------------------------------------------------------
# TASK 4: Write a Python Code to test diiferent types of data-types
# -------------------------------------------------------------------------------

# PYTHON OPERATORS
"""
python operators are used to perform mathematical operations on varaibles and values

Arithmetic Operators -> + - * / % ** //
Assignment Operators -> = += -= *=
Relational Operators -> == != < <= > >=
Logical Operators -> and not or

Read More:
    https://www.geeksforgeeks.org/python-operators/

"""
# Arithmetic Operators -> + - * / % ** //

a = 100
b = 12

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)

print('=' * 80)
# -------------------------------------------------------------------------------
# TASK 5: Write a Python Code to take average of three subject marks.
# -------------------------------------------------------------------------------

# Assignment Operators -> = += -= *=

a = 6
a = a + 5
a += 5
print(a)
print('=' * 80)
# Relational Operators -> == != < <= > >=
# returns boolean value - True False
a = 45
b = 23

print(a > b)
print(a < b)
print('=' * 80)
# -------------------------------------------------------------------------------
# TASK 6: Write a Python Code for Relational Operators
# -------------------------------------------------------------------------------

# Logical Operators -> and not or

x = True
y = False

print(x and y)
print(x or y)
print(not x)
print(not y)

print('=' * 80)
# INPUT AND OUTPUT IN PYTHON

"""
to take input there is input function in python
input()

to display output there is print function in python
print()
"""
a = int(input("Enter Num1"))
b = int(input("Enter Num2"))

print(a * b)
print('=' * 80)
# note a = int(input("Enter Num1")) why i written int in front of this research
# and find the valid answer for this

# -------------------------------------------------------------------------------
# TASK 6: Write a python program to take input from user name , age and date of birth
# and display a dynamic greeting message from the given input
# -------------------------------------------------------------------------------


# CONDITIONAL STATEMENTS
"""
conditional statements in python languages decide the direction or flow of program
execution

- if
- if-else
- elif
- ladder
- nested

"""

# if

"""
if test expr:
    stmt(s)

In python the body of the if statement is indicated by the indentation.
body starts with an indentation and the first unindented line maks the end

the body if is executed only if test expression evaluates to True

"""

age = 22
if age > 18:
    print("You can Vote!")
print('Thank You!')

# if-else


"""
if test expr:
    body
else:
    body

"""

age = 22
if age > 18:
    print("You can Vote!")
else:
    print("You cannot Vote!")

print('Thank You!')

# if..elif..else

"""
if test expr:
    body
elif test expr:
    body
else:
    body
"""
print('=' * 80)
num = 34.4

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")

print('=' * 80)
# -------------------------------------------------------------------------------
# TASK 7: Write the above program again take input from user.
# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# TASK 7: Practice more programs from google till this topic
# https://www.w3resource.com/python-exercises/
# -------------------------------------------------------------------------------


"""
Knowledge is of no value unless you put it into practice.
-Anton Chekhov
"""

# RANGE IN PYTHON

"""
- range() function generate a sequence of numbers
- we can also define the start,stop and step size as range(start,stop,size).
 step size defaults to 1  if not provided

- read more
https://www.w3schools.com/python/ref_func_range.asp
"""

print(list(range(10)))
print(list(range(5, 11, 2)))

# LOOPS IN PYTHON

# for loop

"""
The for loop in python is used to iterate over a sequence (list , tuple , string)
or other iterable objects.
Iterating over a sequence is called traversal

for val in seq:
    body
"""

for x in range(11):
    print(x, end=" ")

a = [1, 2, 3, 4, 76]

for pr in a:
    print(pr)

# while loop
"""
The while loop in python is used to iterate over a block of code as long as the
test expression (condition) is true.

We generally use this loop when we don't know beforehand , the number of times to
iterate

while test_expr:
    body
"""

n = 5

while n >= 0:
    print(n)
    n -= 1

# -------------------------------------------------------------------------------
# TASK 8: https://www.geeksforgeeks.org/loops-in-python/
# Explore break and continue keyword in python
# -------------------------------------------------------------------------------

# BREAK AND CONTINUE IN PYTHON
for i in range(10):
    if i > 6:
        break
    print(i)

for i in range(10):
    if i > 6:
        continue
    print(i)

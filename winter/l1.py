"""
You should understand the following concepts after finishing this notebook:
- variable, data type, number, string
- type conversion
- if statement, boolean statement

This notebook is a very basic introduction to Python. It is meant to be run in a Jupyter notebook, but you may also run it in a Python interpreter.
- Vocabulary are in **bold text**. Knowing them will be very useful for Googling.
- Code snippets are in `monospace`.
- Comments starts with the `#` symbol; they will be ignored by the Python interpreter.
- Run all following cells, including the ones that would not work to familiarize yourself with the error messages.
"""

"""
The `print` function displays values of variables or constants onto thee screen.
"""
print("Hello world")


"""
# Variables and Basic Types
It is at times useful to think of variables as places to store values. The variable `x` refers to a certain space, `y` another. You may change the values stored in these spaces, but before doing that, you need to define the variables.
To define an variable, we use the command `variable_name = value`. Note that you are also assigning a value to that variable.
Basic **data types** include numbers (`int` and `float`), and strings (`str`)
First, we look at numbers.
## Numbers (`int` and `float`)
"""
myint = 7
print(myint)

myfloat = 7.0
print(myfloat)

"""
Some operations you can do with numbers
"""
one = 1
two = 2
three = one + two
print(three)

"""
Some more operations
"""
number = 1 + 2 * 3 / 4.0
print(number)

remainder = 11 % 3
print(remainder)

squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

"""
## Strings (`str`)

The second basic data type in python is **string** (`str`), which represent a sequence of characters.
Strings are enclosed in (either single or double) quotation marks.
"""
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

mystring = "Don't worry about apostrophes. If you want an apostrophe (single quotation mark) in your string, just use double quotation marks to enclose the string."
print(mystring)

"""
You may concatenate multiple strings using `+`.
"""
hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)


"""
## Converting types
"""
# Since not all variables are strings, the following will not work!
one = 1
two = 2
hello = "hello"

print(one + two + hello)

"""
You can convert between types using `typename(variable)`.
Type names include `int` for integer, `float` for floating point numbers, and `str` for strings.
"""
number = 15
print(str(number))
print(float(number))
"""
"""
string = "10"
print(int(string))
print(float(string))
print(float("10.123"))

"""
Of course, you can only convert a string into a number if the string may be interpreted as a number (resp. integer).
For example, the following will not work. Try them!
"""
print(float("abc"))
print(int("10.282"))

"""
A note on types: you may check the type of a variable using the `type` function. This is very useful when debugging.
"""
a = 1
b = 1.0
c = "1"
print(type(a))
print(type(b))
print(type(c))


"""
# Conditionals
In this section we learn the `if` statement. It is often paired with one of multiple `elif` (else if) statements, and an `else` statement.
We first distinguish between the `==` and `=` operators. The former is used to compare two values, while the latter is used to assign a value to a variable.
"""
x = 2
print(x == 2)
print(x == 3)
print(x < 3)
"""
Note that python will evaluate the **boolean statements** `x == 2` etc. to produce a boolean value --- a `True` or a `False`. To check this we again use the `type` function.
"""
print(type(x == 2))

"""
You may use `and` and `or` to combine multiple boolean statements, and `not` to negate a boolean statement.
Use parentheses to make your code more readable.
"""
x = 2
y = 3
print(x == 2 and y == 3)
print(x == 2 and y == 4)
print(x == 2 or y == 4)
print(x == 3 or y == 4)
print(not x == 3)
print((not x == 2) and y == 3)


"""
"""
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

"""
"""
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

"""
"""
statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True: # else if
    # do something else
    pass
else:
    # do another thing
    pass

"""
"""
x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")

"""
"""
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False

"""
"""
print(not False) # Prints out True
print((not False) == (False)) # Prints out False





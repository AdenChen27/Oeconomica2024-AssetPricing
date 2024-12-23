"""
# Variables and Basic Data Types

Note: These notebooks are designed to quickly introduce to *programming*, not *computer science*.

- You do not need to know exactly how everything works, but make sure you have a rough idea of what each line of code means.
- Your final goal is to know how to code (with aid of the Internet).
- You may skip over all explanation, but do run all the code.
- The explanations are terse. If you have question, Google. If you don't, find some question to Google.

Knowing how to Google and ChatGPT is vary useful, but to be a Good Googler, you'll need to know the correct vocabulary, which is displayed in **bold** in this notebook.

After completing this notebook, you should:
- have a rough sense of what a **variable** is
- understand basic **data types** (numbers and strings) and **type conversion**
- know how to perform basic numerical operations (addition, multiplication, division, etc) and string concatenation
- know the `print` function
"""

"""
The `print` function displays values of variables or constants onto the screen.
This is useful for debugging and displaying outputs for the user.
"""
print("Hello world")

"""
# Variables and Basic Types
In Python, **variables** are used to store values. You can think of a variable as a container that holds data.
A variable is defined by giving it a name and assigning a value using the assignment operator `=`.

Basic **data types** include numbers (`int` for integers and `float` for floating-point numbers), and strings (`str` for string).

## Numbers (`int` and `float`)
"""
# Integer
myint = 7
print(myint)

# Float (decimal number)
myfloat = 7.0
print(myfloat)

"""
You can perform operations on numbers such as addition, subtraction, multiplication, and division.
"""
# Basic operations
one = 1
two = 2
three = one + two
print(three)

# More complex operations
number = 1 + 2 * 3 / 4.0
print(number)

# Modulo operation - remainder of a division
remainder = 11 % 3
print(remainder)

# Exponentiation
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)

"""
## Strings (`str`)

**Strings** represent sequences of characters, like words or sentences.
Strings can be enclosed in single quotes `'` or double quotes `"`.

"""
mystring = 'hello'
print(mystring)

mystring = "hello"
print(mystring)

# Handling apostrophes in strings
mystring = "Don't worry about apostrophes. If you want an apostrophe (single quotation mark) in your string, just use double quotation marks to enclose the string."
print(mystring)

"""
You can concatenate (combine) strings using the `+` operator.
"""
hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

"""
## Converting types

Sometimes, you might need to convert a variable from one **data type** to another. 
In Python, you can do this using type conversion functions, such as `int()`, `float()`, and `str()`.

"""
# Trying to add an integer and a string (this will cause an error)
one = 1
two = 2
hello = "hello"

# Uncomment the line below to see the error
# print(one + two + hello)  # This will give an error because you cannot add a string and integers directly

"""
You can convert between types using functions like `int()`, `float()`, and `str()`.
"""
number = 15
print(str(number))
print(float(number))

string = "10"
print(int(string))
print(float(string))

print(float("10.123"))

"""
Of course, you can only convert a string into a number if the string can be interpreted as a valid number.
For example, the following will not work because "abc" cannot be converted into a float or integer.

Try to run these lines to see the error!
"""
print(float("abc"))
print(int("10.282"))

"""
A note on types: You can check the type of a variable using the `type()` function.
This is very useful for debugging and understanding what kind of data you're working with.
"""
a = 1
b = 1.0
c = "1"
print(type(a))
print(type(b))
print(type(c))



"""
# Exercise:

Write code that performs the following:
- create a new variable `x`, with value 2
- set `y` to 2^(x^(x^x)), where ^ stands for exponentiation. Note: 2^(x^(x^x)) is not a valid Python expression (at least it does not mean what you think it means), so turn it into one.
- convert `y` into a string and print it
"""
pass # this is just a placeholder for you code

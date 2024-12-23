"""
You should understand the following concepts after finishing this notebook:
- **variable**, **data type**, **number**, **string**
- **type conversion**
- **if statement**, **boolean statement**

This notebook is a very basic introduction to Python. It is meant to be run in a Jupyter notebook, but you may also run it in a Python interpreter.
- **Vocabulary** are in **bold text**. Knowing them will be very useful for Googling.
- **Code snippets** are in `monospace`.
- Comments start with the `#` symbol; they will be ignored by the Python interpreter.
- Run all the following cells, including the ones that would not work to familiarize yourself with the error messages.
"""

"""
The `print` function displays values of variables or constants onto the screen.
This is useful for debugging and displaying outputs for the user.
"""
print("Hello world")  # Prints "Hello world" to the screen

"""
# Variables and Basic Types
In Python, **variables** are used to store values. You can think of a variable as a container that holds data.
A variable is defined by giving it a name and assigning a value using the assignment operator `=`.

Basic **data types** include numbers (`int` for integers and `float` for floating-point numbers), and strings (`str` for text).

## Numbers (`int` and `float`)
"""
# Integer
myint = 7
print(myint)  # Prints 7

# Float (decimal number)
myfloat = 7.0
print(myfloat)  # Prints 7.0

"""
You can perform operations on numbers such as addition, subtraction, multiplication, and division.
"""
# Basic operations
one = 1
two = 2
three = one + two  # Adding integers
print(three)  # Prints 3

# More complex operations
number = 1 + 2 * 3 / 4.0  # Order of operations is respected (PEMDAS)
print(number)  # Prints 2.5

# Modulo operation - remainder of a division
remainder = 11 % 3
print(remainder)  # Prints 2 (11 divided by 3 leaves a remainder of 2)

# Exponentiation
squared = 7 ** 2  # 7 raised to the power of 2
cubed = 2 ** 3  # 2 raised to the power of 3
print(squared)  # Prints 49
print(cubed)  # Prints 8

"""
## Strings (`str`)

**Strings** represent sequences of characters, like words or sentences.
Strings can be enclosed in single quotes `'` or double quotes `"`.

"""
mystring = 'hello'  # A string enclosed in single quotes
print(mystring)  # Prints hello

mystring = "hello"  # A string enclosed in double quotes
print(mystring)  # Prints hello

# Handling apostrophes in strings
mystring = "Don't worry about apostrophes. If you want an apostrophe (single quotation mark) in your string, just use double quotation marks to enclose the string."
print(mystring)  # Prints the string with an apostrophe

"""
You can concatenate (combine) strings using the `+` operator.
"""
hello = "hello"
world = "world"
helloworld = hello + " " + world  # Concatenate with a space between them
print(helloworld)  # Prints hello world

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
print(str(number))  # Converts the integer to a string, prints "15"
print(float(number))  # Converts the integer to a float, prints 15.0

string = "10"  # A string representation of a number
print(int(string))  # Converts the string to an integer, prints 10
print(float(string))  # Converts the string to a float, prints 10.0

print(float("10.123"))  # Converts the string to a float, prints 10.123

"""
Of course, you can only convert a string into a number if the string can be interpreted as a valid number.
For example, the following will not work because "abc" cannot be converted into a float or integer.

Try to run these lines to see the error!
"""
# Uncomment to test error handling
# print(float("abc"))  # This will give an error because "abc" is not a valid number
# print(int("10.282"))  # This will give an error because "10.282" is a float, not an integer

"""
A note on types: You can check the type of a variable using the `type()` function.
This is very useful for debugging and understanding what kind of data you're working with.
"""
a = 1
b = 1.0
c = "1"
print(type(a))  # Prints <class 'int'>
print(type(b))  # Prints <class 'float'>
print(type(c))  # Prints <class 'str'>

"""
# Conditionals

In this section, we learn about **conditionals**. Conditionals allow your program to make decisions and execute different code based on certain conditions.

The most common conditional is the `if` statement. You can also use `elif` (else if) and `else` to specify additional conditions.

First, let's look at how to compare values. In Python, `==` is used to check equality, while `=` is used for assignment (giving a variable a value).
"""
x = 2
print(x == 2)  # Checks if x is equal to 2, prints True
print(x == 3)  # Checks if x is equal to 3, prints False
print(x < 3)   # Checks if x is less than 3, prints True

"""
Note that Python evaluates boolean expressions like `x == 2` to produce **boolean values**: `True` or `False`.
You can check the type of a boolean value using the `type()` function.

"""
print(type(x == 2))  # Prints <class 'bool'> because x == 2 is a boolean expression

"""
You can combine multiple boolean expressions using `and`, `or`, and negate them using `not`.

- `and` returns True only if both conditions are True.
- `or` returns True if at least one condition is True.
- `not` negates the boolean value.

Using parentheses `()` makes your code more readable and prevents confusion with operator precedence.
"""
x = 2
y = 3
print(x == 2 and y == 3)  # True, both conditions are True
print(x == 2 and y == 4)  # False, second condition is False
print(x == 2 or y == 4)   # True, first condition is True
print(x == 3 or y == 4)   # False, both conditions are False
print(not x == 3)         # True, negates the boolean value
print((not x == 2) and y == 3)  # False, first condition is False

"""
We can now use these boolean values in `if` statements.
"""
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")  # This will print because both conditions are True.

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")  # This will print because the first condition is True.

"""
Instead of using multiple `or` statements, you can also check if a value is in a list using `in`.
"""
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")  # This will print because "John" is in the list.

"""
Now let's look at more complex conditionals with `if`, `elif`, and `else`.

The `elif` keyword allows you to check additional conditions if the previous conditions weren't true.
The `else` keyword is used when none of the conditions match.
"""
statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True:  # else if
    # do something else
    pass
else:
    # do something else if none of the conditions are true
    pass

"""
Simple `if` statement example:
"""
x = 2
if x == 2:
    print("x equals two!")  # This will print because the condition is True.
else:
    print("x does not equal to two.")  # This won't run.

"""
# Comparison between lists
You can compare lists, but remember that `==` checks for equality of contents, while `is` checks if two objects are the same.
"""
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)  # True, because the contents of x and y are the same
print(x is y)  # False, because x and y are two different objects in memory

"""
# Boolean values and negation
"""
print(not False)  # Prints True, because the negation of False is True
print((not False) == (False))  # Prints False, because not False is True, and True == False is False

"""
# Lists and Tuples

In Python, **lists** and **tuples** are used to store collections of items. They are both sequences that can hold multiple values of different data types, but there are some important differences between them.

## Lists

A **list** is an ordered collection of items. Lists are **mutable**, meaning that you can change their contents (e.g., add, remove, or modify elements) after they have been created. Lists are defined using square brackets `[]`.

You can add, remove, and modify items in a list.

"""
# Define a list
my_list = [1, 2, 3, 4, 5]
print(my_list)  # Prints the entire list: [1, 2, 3, 4, 5]

# Accessing elements of a list by index (indexing starts from 0)
print(my_list[0])  # Prints 1 (the first element of the list)
print(my_list[3])  # Prints 4 (the fourth element of the list)

# Modifying a list element
my_list[2] = 10  # Changes the third element (index 2) from 3 to 10
print(my_list)  # Prints the updated list: [1, 2, 10, 4, 5]

# Adding an element to the list
my_list.append(6)  # Adds 6 to the end of the list
print(my_list)  # Prints the list after appending 6: [1, 2, 10, 4, 5, 6]

# Inserting an element at a specific index
my_list.insert(1, 20)  # Inserts 20 at index 1
print(my_list)  # Prints the list after insertion: [1, 20, 2, 10, 4, 5, 6]

# Removing an element by value
my_list.remove(10)  # Removes the first occurrence of 10
print(my_list)  # Prints the list after removing 10: [1, 20, 2, 4, 5, 6]

# Removing an element by index
my_list.pop(3)  # Removes the element at index 3 (which is 4)
print(my_list)  # Prints the list after popping index 3: [1, 20, 2, 5, 6]

# Length of a list
print(len(my_list))  # Prints the length of the list: 5

# Nested list (a list within a list)
nested_list = [1, 2, [3, 4], 5]
print(nested_list[2])  # Prints [3, 4], the sublist at index 2

"""
## Tuples

A **tuple** is similar to a list, but it is **immutable**, meaning that once you create a tuple, you cannot change its contents. Tuples are defined using parentheses `()`.

Since tuples are immutable, they are often used when you want to ensure that the collection of items cannot be altered.

"""
# Define a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)  # Prints the entire tuple: (1, 2, 3, 4, 5)

# Accessing elements of a tuple by index (indexing starts from 0)
print(my_tuple[0])  # Prints 1 (the first element of the tuple)
print(my_tuple[3])  # Prints 4 (the fourth element of the tuple)

# Attempting to modify a tuple (this will cause an error)
# Uncomment the line below to see the error:
# my_tuple[2] = 10  # This will raise a TypeError because tuples are immutable

# Length of a tuple
print(len(my_tuple))  # Prints the length of the tuple: 5

# Nested tuple (a tuple within a tuple)
nested_tuple = (1, 2, (3, 4), 5)
print(nested_tuple[2])  # Prints (3, 4), the subtuple at index 2

"""
## Differences Between Lists and Tuples

- **Lists** are mutable: You can change, add, and remove elements.
- **Tuples** are immutable: Once created, their contents cannot be changed.
- Lists are usually used when you need to modify the contents.
- Tuples are often used for fixed data or when you want to ensure that the data cannot be altered.

You can convert a list to a tuple and vice versa using `tuple()` and `list()`.

"""
# Converting a list to a tuple
list_to_tuple = tuple(my_list)
print(list_to_tuple)  # Prints the tuple: (1, 20, 2, 5, 6)

# Converting a tuple to a list
tuple_to_list = list(my_tuple)
print(tuple_to_list)  # Prints the list: [1, 2, 3, 4, 5]

"""
# Tuple unpacking

In addition to accessing elements by index, you can unpack a tuple into multiple variables.
"""
a, b, c, d, e = my_tuple  # Unpacks the tuple into variables a, b, c, d, e
print(a, b, c, d, e)  # Prints: 1 2 3 4 5

"""
## Iterating Over Lists and Tuples

You can iterate over the elements in a list or tuple using a `for` loop.
"""
# Iterating over a list
for item in my_list:
    print(item)  # Prints each item in the list one by one

# Iterating over a tuple
for item in my_tuple:
    print(item)  # Prints each item in the tuple one by one

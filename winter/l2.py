"""
# Conditionals

Note: These notebooks are designed to quickly introduce to *programming*, not *computer science*.

- You do not need to know exactly how everything works, but make sure you have a rough idea of what each line of code means.
- Your final goal is to know how to code (with aid of the Internet).
- You may skip over all explanation, but do run all the code.
- The explanations are terse. If you have question, Google. If you don't, find some question to Google.

Knowing how to Google and ChatGPT is vary useful, but to be a Good Googler, you'll need to know the correct vocabulary, which is displayed in **bold** in this notebook.


In this section, we learn about **conditionals**.
Conditionals allow your program to make decisions and execute different code based on certain conditions.
The most common conditional is the `if` statement. 
You can also use `elif` (else if) and `else` to specify additional conditions.

After completing this notebook, you should know how to write conditional statements with `if`, `elif`, and `else`.
"""
"""
First, let's look at how to compare values. In Python, `==` is used to check equality, while `=` is used for assignment (giving a variable a value).
"""
x = 2
print(x == 2)
print(x == 3)
print(x < 3)

"""
Note that Python evaluates boolean expressions like `x == 2` to produce **boolean values**: `True` or `False`.
You can check the type of a boolean value using the `type()` function.
"""
print(type(x == 2))

"""
The *value* of the *expression* `x == 2` is **boolean**. Just like numbers and strings, it is a basic data type.
And just like any number or string, you may store a boolean value.

In full detail, the following line of code checks if x equals 2 with the boolean expression x == 2, and store the truth value of this statement in `x`.
"""
x_is_2 = (x == 2)
print(x_is_2) 


"""
You can combine multiple boolean expressions using `and`, `or`, and negate them using `not`.

- `and` returns True only if both conditions are True.
- `or` returns True if at least one condition is True.
- `not` negates the boolean value.

Using parentheses `()` makes your code more readable and prevents confusion with operator precedence.
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
We can now use these boolean values in `if` statements.
Note that a if statement always have the following format:

if [boolean statement]:
    [code to run when the boolean statement is true]

[Other commands outside of the if statement]

Note:
- There must be a colon after the boolean statement.
- You may have multiple lines of code in [code to run when the boolean statement is true]. But they must all be indented at the same level. This is Python's way to tell what part of the code is part of the if statement.
- When in doubt, Google.
"""
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")  # This will print because both conditions are True.

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")  # This will print because the first condition is True.


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
# Exercise:
Write code to test whether x is a multiple of 2 and 3, but not 7
"""

x = 653184
# fill out the following template:
if ...:
    print("x is a multiple of 2 and 3, but not 7")
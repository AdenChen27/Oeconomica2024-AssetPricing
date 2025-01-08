"""
# Functions

Note: These notebooks are designed to quickly introduce to *programming*, not *computer science*.

- You do not need to know exactly how everything works, but make sure you have a rough idea of what each line of code means.
- Your final goal is to know how to code (with aid of the Internet).
- You may skip over all explanation, but do run all the code.
- The explanations are terse. If you have question, Google. If you don't, find some question to Google.

Knowing how to Google and ChatGPT is vary useful, but to be a Good Googler, you'll need to know the correct vocabulary, which is displayed in **bold** in this notebook.

You've seen plenty of examples of functions.
It's time to formally introduce them.
"""

"""
In Python, you can call a function by using its name followed by parentheses `()`. If the function requires arguments, you pass the values inside the parentheses.
"""
# Calling the print function
print("Hello!")

"""
In this example, we called the **`print()`** function to display a message. The **argument** passed to the `print()` function is `"Hello!"`. An **argument** is the value or information that you pass into a function when calling it.

## Arguments

Arguments are the values you send to a function when calling it. These values are used by the function to perform its task. Functions can accept multiple arguments, and the number and type of arguments the function accepts will depend on how the function is defined.

### Example:

Let’s use the built-in `len()` function, which returns the length of an object (like a list or a string). The argument we pass to `len()` will be the object whose length we want to know.
"""

# Using the len() function to find the length of a string
course_name = "Economics 101"
course_length = len(course_name)
print(f"The course name '{course_name}' has {course_length} characters.")

"""
Here, we called the **`len()`** function and passed the string `"Economics 101"` as an argument. The function then returned the length of the string, which is 15, and we printed the result.

## Defining Your Own Function

You can define your own functions using the `def` keyword. A function can take one or more arguments and return a value.

### Example:

Let’s define a simple function that calculates the total cost based on the price and quantity of a product. The function will take two arguments: **price** and **quantity**.
"""

# Defining a custom function
def calculate_total_cost(price, quantity):
    total_cost = price * quantity
    return total_cost

# Calling the custom function with arguments
price_per_item = 20
quantity_purchased = 3
total_cost = calculate_total_cost(price_per_item, quantity_purchased)

print(f"The total cost for {quantity_purchased} items at ${price_per_item} each is: ${total_cost}")

"""
It is good practice to wrap often-used pieces of code in functions!
"""

"""
# Exercise 1:

Define a function that takes in two numbers as input and outputs their product.
"""
#EMPTYCELL

"""
# Exercise 2

Google "python **typing**" and "mypy" and read about it. (Find out the difference between `mypy` and python's default type checking system. Why is `mypy` better?) Add type hints using typing for the function you defined above.
*Always* use typing when possible. It will save you loads of time debugging.
"""
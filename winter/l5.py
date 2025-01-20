"""
# Functions

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

"""
# Exercise 3

Define a function that takes in two lists as input, interpret them as vectors, and outputs their distance.
"""
#EMPTYCELL


"""
# Exercise 4

Using your function above, define a new function that takes in a list `vec` of length 3 as input and outputs the sum of
1. the distance between `vec` and the vector (1, 4, 6)
2. the distance between `vec` and the vector (2, 8, 3)
3. the distance between `vec` and the vector (7, 1, 9)
"""
#EMPTYCELL

"""
# Exercise 5

Find an approximate minimum of the function you defined above and the input that achieves that (approximate) minimum. (This is know as the Fermat point.)

You may proceed in the following steps:
1. Narrow the search space down. An educated guess is that if the minimum is attained at (x, y, z), then we know -100 <= x <= 100. You can narrow it down further.
2. We calculate the value of the function on a subset of points in our search space. The finer the set of points, the more accurate our solution will be.

You can start with something like this (you will need to import numpy using `import numpy as np` to use the function `np.linspace`):
```python
for x in np.linspace(x_min, x_max, N):
    for y in np.linspace(y_min, y_max, N):
        for z in np.linspace(z_min, z_max, N):
            calculate the function value at (x, y, z)
```
Find out what `np.linspaec` does [here](https://numpy.org/doc/2.1/reference/generated/numpy.linspace.html).
What does `N` do?
"""
import numpy as np

#ANSWER
import numpy as np
N = 100
x_min = y_min = z_min = 0
x_max = y_max = z_max = 10

cur_min_vec = (0, 0, 0)
for x in np.linspace(x_min, x_max, N):
    for y in np.linspace(y_min, y_max, N):
        for z in np.linspace(z_min, z_max, N):
            if f((x, y, z)) < f(cur_min_vec):
                cur_min_vec = (x, y, z)


"""
Such optimization problems are extreme common in economics.
Oftentimes, analytic solutions can be hard to even impossible to find, and your only resort will be to find approximate solutions computationally.
"""

"""
# Exercise 6

Solve the problem above using gradient descent. (Yes, of course for this problem you can find the solution analytically by setting the gradient to zero.)
Hint: the gradient at `(x, y, z)` is `(2*(3*x - 10), 2*(3*y - 13), 2*(3*z - 17))`.
"""
#EMPTYCELL
#ANSWER
epsilon = 0.0001
x, y, z = cur_min_vec

for i in range(100):
    x += epsilon*(-1)*(3*x - 10)
    y += epsilon*(-1)*(3*y - 13)
    z += epsilon*(-1)*(3*z - 17)

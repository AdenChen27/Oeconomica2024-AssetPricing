"""
# Tuples, Lists, and Dictionaries

Note: These notebooks are designed to quickly introduce to *programming*, not *computer science*.

- You do not need to know exactly how everything works, but make sure you have a rough idea of what each line of code means.
- Your final goal is to know how to code (with aid of the Internet).
- You may skip over all explanation, but do run all the code.
- The explanations are terse. If you have question, Google. If you don't, find some question to Google.

Knowing how to Google and ChatGPT is vary useful, but to be a Good Googler, you'll need to know the correct vocabulary, which is displayed in **bold** in this notebook.

After completing this notebook, you should understand three **data types**:
- **Tuples**: Ordered, immutable collections of values.
- **Lists**: Ordered, mutable collections that can be modified.
- **Dictionaries**: Collections of key-value pairs, where each key is unique.
"""

"""
## Tuples

A **tuple** is an ordered collection of values that is **immutable**, meaning that once created, you cannot change the values inside a tuple. Tuples are commonly used when you need to store a fixed set of values, like coordinates or months in a year.
"""
# Create a tuple for product prices
product_prices = (19.99, 35.50, 12.75)
print(product_prices)

"""
Here, `product_prices` is a **tuple** containing three values. You cannot change any of these values after the tuple is created.

### Accessing Tuple Elements

You can access individual elements of a tuple using their **index** (accessing by index is sometimes called **indexing**), starting from 0. 
You can also count backwards by using negative integers, starting from -1.
"""

# Accessing the second element of the tuple
second_price = product_prices[1]
print(f"The price of the second product is: ${second_price}")
last_price = product_prices[-1]
print(f"The price of the last product is: ${last_price}")

"""
You can **nest** tuples inside tuples.
"""
# Nested tuple (a tuple within a tuple)
nested_tuple = (1, 2, (3, 4), 5)
print(nested_tuple[2])


"""
## Lists

A **list** is similar to a tuple, but unlike a tuple, lists are **mutable**. This means you can add, remove, or change elements of a list. Lists are often used when you need to store an ordered collection of items that may change over time.

### Example:

Let's create a list to store the number of students enrolled in different economics courses.
"""
students_in_courses = [30, 45, 25, 50]
print(students_in_courses)

"""
### Modifying Lists

You can change elements in a list using their index or add new elements using methods like `append()`.

### Example:

Let's update the number of students in the second course and add a new course.
"""

# Change the number of students in the second course
students_in_courses[1] = 40
print(f"Updated student list: {students_in_courses}")

# Add a new course with 60 students
students_in_courses.append(60)
print(f"Updated student list after adding a new course: {students_in_courses}")

"""
Recall that you may not alter the elements of a tuple.
Try it:
"""
product_prices = (19.99, 35.50, 12.75)
product_prices[1] = 35

"""
Here are some more operations you can do.
"""
my_list = [1, 2, 3, 4, 5]
print(my_list)  # Prints the entire list: [1, 2, 3, 4, 5]

# Length of a list
print(len(my_list))

# Accessing elements of a list by index (indexing starts from 0)
print(my_list[0])  # Prints 1 (the first element of the list)
print(my_list[3])  # Prints 4 (the fourth element of the list)

# Modifying a list element
my_list[2] = 10  # Changes the third element (index 2) from 3 to 10
print(my_list)

# Adding an element to the list
my_list.append(6)  # Adds 6 to the end of the list
print(my_list)

# Inserting an element at a specific index
my_list.insert(1, 20)  # Inserts 20 at index 1
print(my_list)

# Removing an element by value
my_list.remove(10)
print(my_list)

# Removing an element by index
my_list.pop(3)
print(my_list)

# Nested list (a list within a list)
nested_list = [1, 2, [3, 4], 5]
print(nested_list[2])

"""
Recall conditionals.
Another often used boolean expression is `A in B`, which checks whether `A` is an element of the list/tuple `B`.
"""
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")
if name in ("John", "Rick"): # You can also use a tuple
    print("Your name is either John or Rick.")


"""
## Dictionaries

A **dictionary** is a collection of **key-value pairs**. Each key in a dictionary must be unique, and each key is associated with a value. Dictionaries are useful for storing data where you need to look up a value based on a key, like looking up a student's name based on their ID.

### Example:

Let's create a dictionary to store the number of students in various courses, with the course names as keys.
"""

# Create a dictionary to store course student counts
course_student_counts = {
    "Economics 101": 30,
    "Microeconomics": 45,
    "Macroeconomics": 25
}
print(course_student_counts)

"""
Here, `course_student_counts` is a **dictionary** where each key is a course name, and the value is the number of students enrolled in that course.

### Accessing Dictionary Elements

You can access the value associated with a key by using square brackets `[]` with the key.
"""
students_in_microeconomics = course_student_counts["Microeconomics"]
print(f"Students in Microeconomics: {students_in_microeconomics}")

"""
You can modify the value associated with a key or add new key-value pairs.
"""
# Update the number of students in Macroeconomics
course_student_counts["Macroeconomics"] = 30
print(f"Updated course list: {course_student_counts}")

# Add a new course
course_student_counts["Statistics 101"] = 50
print(f"Updated course list after adding Statistics 101: {course_student_counts}")





"""
Note that list, tuple, and dictionary are all data types.
You may use `list` and `tuple` to convert lists to tuples and vice versa.
"""
a = (1, 2, 3)
print(a, type(a))
a = list(a)
print(a, type(a))
a = tuple(a)
print(a, type(a))

"""
Always remember what data type you are dealing with.
Recall that you can use `type` to check the data type.
"""
print(type((1, 2)))
print(type([1, 2]))
print(type({1: 2}))

"""
# Exercise 1

- Go google the `range` function.
Note that `range` returns a generator (you don't have to care too much about what that means for now), but you may convert a generator into a list using `list()`.
- Create a list using the `range` and `list` functions that contains all multiples of 7 from 1 to 7777.
- Calculate the sum of these numbers and print it out. (Hint 1: you do not need `for` or `while`, which you will learn in the next notebook. Hint 2: Google. You just need one function that you've never seen.)
"""
#EMPTYCELL

"""
# Exercise 2

- Find a way to obtain a *list* containing all keys of a given dictionary. (For the following dictionary, you should obtain ["a", "b", "c", "d"]).
- Find a way to obtain a *tuple* containing all values of a given dictionary. (For the following dictionary, you should obtain [1, 2, 3, 4]).
- Use Google.
"""
d = {"a": 1, "b": 2, "c": 3, "d": 4}

"""
# Exercise 3

- Go learn about the data type **set**.
"""
#EMPTYCELL
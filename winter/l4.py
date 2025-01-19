"""
# Loops

Note: These notebooks are designed to quickly introduce to *programming*, not *computer science*.

- You do not need to know exactly how everything works, but make sure you have a rough idea of what each line of code means.
- Your final goal is to know how to code (with aid of the Internet).
- You may skip over all explanation, but do run all the code.
- The explanations are terse. If you have question, Google. If you don't, find some question to Google.

Knowing how to Google and ChatGPT is vary useful, but to be a Good Googler, you'll need to know the correct vocabulary, which is displayed in **bold** in this notebook.

After completing this notebook, you should:
- understand what loops are and how to write basic `for` and `while` loops
- understand how and when to use `continue` and `break`
"""

"""
## `for` Loop

A **`for` loop** is used to iterate over a sequence (such as a list, tuple, string, or range) and perform an action for each element in the sequence.
It’s commonly used when you know the number of iterations or when you're working with a collection of data.
"""
# Create a list of course names
courses = ["Economics 101", "Microeconomics", "Macroeconomics", "Statistics 101"]

# Using a for loop to iterate over the courses
for course in courses:
    print(course)

"""
In this example, the **`for` loop** iterates through the `courses` list, and for each iteration, the variable `course` takes the value of the next item in the list. The loop then prints each course name.

### Using the `range()` Function with `for` Loop

The `range()` function generates a sequence of numbers and is often used with `for` loops when you need to perform an action a specific number of times.

### Example:

Let's print numbers from 1 to 5 using a `for` loop.

"""

# Using range() to generate numbers from 1 to 5
for number in range(1, 6):
    print(number)

"""
Here, `range(1, 6)` generates the numbers 1, 2, 3, 4, and 5. The **`for` loop** iterates over these numbers and prints each one.
"""

"""
## `while` Loop

A **`while` loop** repeatedly executes a block of code as long as a specified condition is true. It's useful when you don't know the exact number of iterations in advance, but you have a condition that needs to be met.
"""
number = 1
while number <= 5:
    print(number)
    number += 1  # Increment the number by 1

"""
In this example, the **`while` loop** continues to execute as long as the condition `number <= 5` is true. After each iteration, we increment the `number` variable by 1 to avoid an infinite loop.
"""

"""
### Infinite Loop

Be cautious with `while` loops, as it's easy to create an **infinite loop** if the loop condition never becomes false. For example:
"""
while True:
    print("This will run forever!")

"""
## Exercise 1:
Google how to use `continue` and `break`.
Make sure you understand the difference between the following two loops.
"""
for number in range(1, 6):
    if number == 3:
        break
    print(number)

for number in range(1, 6):
    if number == 3:
        continue
    print(number)

"""
## Exercise 2:
Run a for loop on a dictionary. What happens? What are you looping over?
"""
#EMPTYCELL

"""
## Exercise 3:
In a previous notebook, you calculated the sum of all integer multiples of 7 between 1 and 7777 using the `sum` function.
This time do the same thing using a for loop.

Hint 1: you do not need to use a list to store the relevant numbers.

Hint 2: in each iteration, add to your sum one more number.
"""
#EMPTYCELL

"""
Hint 3:
your code should look something like:
```
sum_of_numbers = 0
for all x such that 1 <= x <= 7777:
    if x a multiple of 7:
        sum_of_numbers += x
```
the last line of which is equivalent to `sum_of_numbers = sum_of_numbers + x`.
"""

"""
## Exercise 4:

1. Using a for loop, find the *first* occurrence of the character "T" in the following DNA sequence.
2. Using a for loop, find *all* occurrences of the character "T" in the following DNA sequence. You should obtain a list of indexes.

Note that these are inverses of "indexing."

Hint: you might need to use `break` or `continue`.
"""
string = 'GCGGTCATCTTTGCACCTAAGACAAACACCCGGACACCCATATCTGTCAATCTACGCGTCTGATCTGGTGCATTCCCCATCACAATTTATCCGAATCCTTTGACTTCCTGTCTGTTCCCGGCCGTGTGTAGGTTGACGGCCGACGTAACCCATGGTCGGAACAATTGACGTCCTGACATCCCTGCCGCGATCAACGAGGTGCCCAACACATGGGGTCTATCCTTGCTCGAAATACGAATACGCTGAAGGATATCGTTTATGACCCCTGCGCTAAGCCGGAAAGTCGGTTTGTACCCCACGTCAGGTCGTAAGGAAAACCCGCGGGAGACGAAACAAAGCACTCCACGCCGGTAAGTCTTCGCTGCAATGAAATTCGGACAGTCGCGTACCGTTTCGCGATTCCACCATCCATTCCTCCTAAGATGTCGGCCACTATCATTGCAATGAGGGGGGGCGCCGATACGCCACTCGCGCCACTTTAACCATTAGCGCCTGAATTCGGATTTCACCGTGGTCACTGGAACGAGGCGAATCGGCGCGTAGAGTAGGCCCTATTTTTATCAGCTGAAATGCTGAATACCTCCAACTAAGAATTCATTTATAGCCCCGTTGCTTGCGTGTAGGCAAAATCGAACTCGGCCAAAGCTACCGTGAAGGAGCTGATACCGAATCTATGGATATGGTTCACGTTACGACATCATCCCCGTAATCCGAAAGAGTCGTCGTCAACATGTACCTCAATCGGTTACGCTTATTTGGAGTCCCGTCGTACCTCGACGTCCTATTCACGGGTAGATGCCACGTGGCGTCCGTTTTTGGCACCCCGAGTCATTGCATTTTTCGTTTCCACACAGATTATTAGGCAAACTTTCGCGTAAGCGATTCCCTGTGCCGCACGGTAAAGCCGATGTTTGCAGCAAGCGCCTGTCGTGGAGAGCTTAAATGCAATGAGTAAGTTACAGAGAGGAGTGAGCTGTGCAACACACTGAGACGGTAACTA'

"""
## Exercise 5:

In exercise 4 your obtained a list of indexes where the character "T" occurred in the provided string.
Check using a loop that the list you obtained is correct.
"""
#EMPTYCELL


"""
## Exercise 6:

Find *all* occurrences of the sequence "ATCG" in the string provided above.

Hint: you need to use a nested loop (there are simpler approaches using other string methods, but do make sure you know how to write a nested loop).

(Look up the Knuth–Morris–Pratt algorithm and Aho–Corasick algorithm if you want more efficient solutions. They are much harder to implement.)
"""
#EMPTYCELL

"""
## Exercise 7:

Calculate the dot product of two vectors (provided as lists).
"""
vec1 = [-71, 79, 45, 33, 40, -46, 28, 18, 83, -9, 29, 15, 81, 41, -23, -85, -93, 96, 63, 8, 31, 35, 81, 7, -87]
vec2 = [24, 34, -75, -18, -80, 46, 12, 86, 26, -78, 49, -98, -61, 89, -90, 88, -71, 14, 12, 28, 65, 40, 78, -66, -61]

"""
## Exercise 8:

Find the largest element in the following list and its position without using the function `max`.

Hint: create auxiliary variables storing the position of the maximum among the elements that you have examined.
"""
vec = [-71, 79, 45, 33, 40, -46, 28, 18, 83, -9, 29, 15, 81, 41, -23, -85, -93, 96, 63, 8, 31, 35, 81, 7, -87]

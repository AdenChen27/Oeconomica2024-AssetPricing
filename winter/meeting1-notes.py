# 1. install brew
# 2. install python
# 3. install jupyterlab (pip install jupyterlab)
# 4. jupyter notebook
# Access the notebooks at: https://github.com/AdenChen27/Oeconomica2024-AssetPricing/tree/main/winter


# Variables (sometimes useful to think of them as places in which you can store data)


# If statements
if [statement 1]:
    block of code
    block of code
elif [statement 2]: # elif == else if
    something you want to run if statement 2 is true
elif [statement 3]:
    something you want to run if statement 3 is true
else:
    something else

if x == 0:
    print("x is 0")
elif x != 0:
    print("x is 0")

# Lists, Tuples, Dictionaries
# Lists
my_list = [1, 2.2, "strings", [1, 2, 3]]
# .append(); .extend()

my_tuple = (1, 2.2, "strings", (1, 2, 3))

# check if element is contained in list/tuple
if student_name in name_list:
    print("Student is in the list")


# Dictionaries
d = {"key1": "value1", "key2": "value2"}
d["new_key"] = "new_value" # adds new key
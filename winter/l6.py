"""
# Pandas: Data Manipulation

Starting from this notebook, there will be a lot less explanation.
Instead, you will be given a sequence of tasks, and you will Google you way through these tasks.
(Hint: start by googling the terms in **bold**.)
(Hint 2: the official pandas documentation should be your fwend.)
"""
"""
# Task 1:
- Go find out what a **.csv** file is.
- Open the csv file `salary-data.csv` using a **text editor** of your choice.
- **Load/Read** the csv file about using pandas into a DataFrame called `df` (hint: use the **`pd.read_csv`** function. Pay attention to the `header` argument.)
"""
import pandas as pd

"""
# Task 2:
- Inspect the csv file in the notebook by running the following code.
"""
df

"""
# Task 3: Indexing
- Find out what a DataFrame is and how it is different from a list or tuple.
- Learn how to **index** a DataFrame.

To practice you indexing skills, do the following:
- Find the row of the DataFrame corresponding to Charlie's data.
- Find the salary column of the DataFrame.
- Obtain a sub-DataFrame that contains only data on Alice, Bob, and Charlie.
- Obtain a sub-DataFrame that contains only data on Alice, Bob, and Charlie, and with only the name, age, and salary columns.
- Obtain a sub-DataFrame that contains data on all persons with age >= 30.
- Obtain a sub-DataFrame that contains data on all persons with age >= 30 and in the Engineering department.
"""
pass

"""
# Task 4: Data Manipulation

- Create a new column "remaining income", with value `salary * (80 - age)`
- Do the above using two methods: (1) use a for loop with iterrows; for a hint, see Task 5. (2) use the DataFrame `apply` method. Make sure you understand both methods.
"""
pass

"""
# Task 5: 

Guess what the following code snippet does:
"""
for i, row in benchmark.iterrows():
    benchmark.at[i, "model-prediction"] = classifier.classify_case(row["dir"])

print((benchmark["human-labeled-outcome"] == benchmark["model-prediction"]).sum() / len(benchmark))

"""
# Task 6: Real Data

Load the `electoral-democracy-index.csv` file, which contains data on V-Dem's country/year-level democracy index.

Locate the data for United States. Find the average democracy score for united states in the 18th, 19th, 20th, and 21th centuries.
Compare them.
"""
pass
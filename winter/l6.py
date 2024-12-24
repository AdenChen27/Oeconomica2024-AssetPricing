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
# Task 6: Democracy

Load the `electoral-democracy-index.csv` file, which contains data on V-Dem's country/year-level democracy index.

- Locate the data for United States. Find the average democracy score for united states in the 18th, 19th, 20th, and 21th centuries. Compare them.
- In what year did the US achieve its highest democracy score? The lowest?
"""
pass

"""
# Task 6: Democratic Backsliding?

Some claim that a global democratic decline has been happening over the past few decades.
We evaluate this claim using V-Dem's democracy index.

Follow the steps below:
- Come up with a measure of democratic backsliding in the past 20 years. This should be a function that takes in the past 20 years of democracy scores for a given country and outputs a single score representing the extent of democratic backsliding for that country. Think of what you might want in such a measure.
- Aggregate the DataFrame that contains democracy score for each country/year to a DataFrame that contains a "backsliding" index for each country. That is, for each country you are aggregating the democracy indexes over the years to one single backsliding index. After this step, you should have a DataFrame that looks something like:

    ```
    Country 1 | backsliding index 1
    Country 2 | backsliding index 2
    Country 3 | backsliding index 3
    ...
    ```

    - Hint 1: use the `DataFrame.aggregate` method with a `func` you defined above.
    - Hint 2: it is often useful to test the functions on a smaller DataFrame when debugging.

- Now find the countries with the most amount of democratic backsliding. (Hint: use the `DataFrame.sorrt_values` function.) 
"""
pass


"""
# Task 7: Democratic Backsliding (continued)?

Democratic backsliding is obviously occurring in *some* countries. But do we have evidence for a *global* democratic backsliding?
You may test this by looking at the average of the "backsliding" score (which you created in the previous task), but this gives each country the same weight. One way to get a global "backsliding" score is to weight each country by its population.
To make life easier, we will use only the indexes for each continent in the dataset.

Follow the steps below:
- Load `population.csv`, which contains data on countries and continents.
- Note that some continents are named differently in the population dataset and in the democracy index dataset. Rename the relevant column of one of these datasets so that the two datasets have the same names.

    Hint: Use a dictionary to store a mapping from the old names to the new (matching) names (e.g. from "Africa (UN)" to "Africa"), and use `.apply` on the column storing names to change old names to the corresponding new names.
- Merge the two datasets so you have the population and democracy index data in the same DataFrame.
    
    Hint: Google `DataFrame.join` and `DataFrame.merge`.

- Calculate a population-weighted "backsliding" score for the past 20 years. Is there a global democratic backslide?
"""
pass

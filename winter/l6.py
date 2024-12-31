"""
# Pandas: Data Manipulation

Starting from this notebook, there will be a lot less explanation.
Instead, you will be given a sequence of tasks, and you will Google you way through these tasks.

Hint 1: start by googling the terms in **bold**.

Hint 2: the official [pandas documentation](https://pandas.pydata.org/docs/) should be your friend.
"""
"""
# csv
- Find out what a **.csv** file is.
- Open the csv file `datasets/salary-data.csv` using a **text editor** of your choice.
- **Load/Read** the csv file about using pandas into a DataFrame called `df` (hint: use the **`pd.read_csv`** function. Do you need the `header` argument?)
"""
import pandas as pd
import numpy as np

"""
Inspect the csv file in the notebook by running the following code.
"""
df

"""
# DataFrame Indexing
- Find out what a DataFrame is and how it is different from a list or tuple.
- Learn how to **index** a DataFrame.

To practice you indexing skills, do the following:
- Find the row of the DataFrame corresponding to Charlie's data.
- Find the salary column of the DataFrame.
- Obtain a sub-DataFrame that contains only the second and third row in the original DataFrame.
- Obtain a sub-DataFrame that contains only data on Alice, Bob, and Charlie.
- Obtain a sub-DataFrame that contains only data on Alice, Bob, and Charlie, and with only the name, age, and salary columns.
- Obtain a sub-DataFrame that contains data on all persons with age >= 30.
- Obtain a sub-DataFrame that contains data on all persons with age >= 30 and in the Engineering department.
"""
#EMPTYCELL

"""
## Vectors

The number-valued columns in `df` can be treated as vectors.
Try the following examples on the simple DataFrame `df2`:
"""
df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
df2
"""
You may add columns as vectors:
"""
print(df2['a'] + df2['b'])
print(df2['b'] + df2['c'])
"""
You may add a scalar to each term of the vector:
"""
print(df2['b'] + 10)
"""
You may multiple a vector by a scalar:
"""
print(10 * df2['a'])
print(11 * df2['c'])
"""
`np.array` is basically the same:
"""
A = np.array([1, 2, 3])
B = np.array([4, 5, 6])
print(A + B)
print(A + 3)
print(3 * A)
"""
Boom! You now know also `numpy`. (Basically.)
"""


"""
# Data Manipulation

Create a new column "remaining lifetime income", with value `salary * (80 - age)`, using all three methods below:
- Treat each column as a vector. Then the "remaining lifetime income" (as a vector) is just `salary * (80 - age)` (each variable interpreted as a vector).
- Use a `for` loop with `iterrows`; for a hint, see the next problem ("Guess"). 
- Use the DataFrame `apply` method. You might want to recall how you can define a function.
"""
#EMPTYCELL

"""
## Guess

Guess what the following code snippet does:
"""
...
for i, row in benchmark.iterrows():
    benchmark.at[i, "model-prediction"] = classifier.classify_case(row["dir"])

print((benchmark["human-labeled-outcome"] == benchmark["model-prediction"]).sum() / len(benchmark))
...

"""
# Democracy

Some claim that a global democratic decline has been happening over the past few decades.
We evaluate this claim using V-Dem's democracy index.

First, load the [`datasets/electoral-democracy-index.csv`](https://ourworldindata.org/democracy) file, which contains data on V-Dem's country/year-level democracy index. Use the [`head`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html) and [`tail`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.tail.html) functions to inspect the first and last few entries of the DataFrame.

- Rename the column containing the democracy indices to something simpler.
- Locate the data for United States. Find the average democracy score for united states in the 18th, 19th, 20th, and 21th centuries. Compare them.
- In what year did the US achieve its highest democracy score? The lowest? (Hint: use the [`DataFrame.sorrt_values`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html) function.)
"""
#EMPTYCELL
#ANSWER
df = pd.read_csv("datasets/electoral-democracy-index.csv")
df = df.rename(columns = {
    'Electoral democracy index (best estimate, aggregate: average)': "Democracy"
})


"""
## Democratic Backsliding: Measurement

We aim to calculate a "backsliding score" for each country in the DataFrame.

First, come up with a measure of democratic backsliding in the past 10 to 20 years (to be concrete, say from year 2010 to 2020). This should be a function that takes in the past 10 years of democracy scores for a given country and outputs a single score representing the extent of democratic backsliding for that country. Think of what you might want in such a measure, and start simple.

Next, use the DataFrame above, which contains democracy score for each country/year, to produce a DataFrame that contains a "backsliding" index for each country. That is, for each country you are aggregating the democracy indexes over the years to one single backsliding index. After this step, you should have a DataFrame that looks something like:

```
Country 1 | backsliding score 1
Country 2 | backsliding score 2
Country 3 | backsliding score 3
...
```

You can follow the template below:
```python
countries = [a list of countries]
backsliding_score = {}
for country in countries:
    [check if you have enough data to calculate a score; is not, skip this country]
    democracy_scores = [the last 10 years of democracy scores for `country`]
    [calculate a backsliding score using your function]
    backsliding_score[country] = [the backsliding score]
```
After running this you will obtain the backsliding scores for each country stored in the dictionary `backsliding_score`.
You can turn the dictionary (for ease of analysis) into a DataFrame using something like:
```python
pd.DataFrame(backsliding_score, index=["Democracy"])
backsliding_df = backsliding_df.transpose()
```
(Why `transpose`?)

Hint:
- You might want to use the [`unique`](https://pandas.pydata.org/docs/reference/api/pandas.unique.html) function to obtain a list of countries.
- If you encounter missing data for just a few countries, just ignore those countries.
- I check the examples in [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) for syntax whenever I want to turn something into a DataFrame.
"""
#EMPTYCELL
#ANSWER
countries = df["Entity"].unique()
backsliding_score = {}

for country in countries:
    start_year = df[(df["Entity"] == country) & (df["Year"] == 2010)]
    end_year = df[(df["Entity"] == country) & (df["Year"] == 2020)]
    
    if start_year.empty or end_year.empty:
        print(f"Missing data for 2000 or 2020: {country}")
        continue

    if "Democracy" not in start_year or "Democracy" not in end_year:
        print(f"Missing 'Democracy' column: {country}")
        continue
    
    score = end_year.iloc[0]["Democracy"] - start_year.iloc[0]["Democracy"]
    backsliding_score[country] = score

backsliding_df = pd.DataFrame(backsliding_score, index=["Democracy"])
backsliding_df = backsliding_df.transpose()

"""
Now, find the countries with the highest democratic backsliding scores.
"""
#EMPTYCELL
#ANSWER
backsliding_df.sort_values(by="Backsliding")


"""
## Democratic Backsliding: Analysis

Democratic backsliding is obviously occurring in *some* countries. But do we have evidence that a *global* democratic backsliding is also happening?
You may test this by looking at the average of the "backsliding" score (which you created in the previous task), but this gives each country the same weight (the experience of citizens living in smaller countries are then arguably over-weighted).
One way to get a global "backsliding" score is to weight each country by its population.
This will weight the experience of citizen in each country equally.

Follow the steps below:
- Load [`datasets/population.csv`](https://ourworldindata.org/population-growth), which contains data on population data at the country-year level.
- Note that almost all country in this DataFrame matches that in the democracy index DataFrame. This is convenient for us. If the country names does not match (e.g. "USA" in one and "US" in another), we will have to rename the columns so that they match.
- Merge the two datasets so you have the population and democracy index data in the same DataFrame. (The `datasets/population.csv` dataset contains population data for each year. For simplicity, let's just use the population in the year 2020 in our analysis.)

    Hint: Use [`DataFrame.join`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html). You might have to change the indexes of one of the DataFrames so that both DataFrames have matching indexes.

- Calculate a population-weighted "backsliding" score for the past 10 years. Do we have evidence for global democratic backsliding?
"""
#EMPTYCELL
#ANSWER
popdf = pd.read_csv("datasets/population.csv")
popdf = popdf.rename(columns = {
    'Population - Sex: all - Age: all - Variant: estimates': "Population"
})

popdf = popdf[popdf["Year"] == 2020]
popdf = popdf.set_index("Entity")
popdf
#NEWCELL
backsliding_df = backsliding_df.join(popdf)
backsliding_df
#NEWCELL
backsliding_df = backsliding_df.dropna()
np.dot(backsliding_df["Population"], backsliding_df["Backsliding"]) / backsliding_df["Population"].sum()

"""
Assuming V-Dem's democracy index perfectly reflects the level of democracy, what else might go wrong in our analysis?
"""
"""
We will conduct a more rigorous analysis using regression.
"""
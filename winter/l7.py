"""
# Pandas: Data Visualization
"""
import pandas as pd
import numpy as np
"""
# Warm up

Install `matplotlib` and use it to plot the following functions:
- $f(x) = x - 1$
- $f(x) = x^7 - x^5$
- $f(x) = \sin(x)$
"""
#EMPTYCELL

"""
# Democracy of the US

Load the [`datasets/electoral-democracy-index.csv`](https://ourworldindata.org/democracy) file, which contains data on V-Dem's country/year-level democracy index.
- Plot United States data over the years as a line plot.
- Fit a polynomial of degree 4 through the data.
- Clearly label you graph.
"""
#EMPTYCELL

"""
# A Comparison

Create a new graph, comparing the democracy scores of the US and the UK (plot data of both countries in the same plot).
"""
#EMPTYCELL

"""
# Probability

(Stolen from Dan Nicolae)

Generate 500 samples of 2 random variables $X_1$ and $X_2$ with distribution $\mathrm{Exponential}(1)$.
For each of the 500 samples, calculate $\min(X_1, X_2)$ $\max(X_1,X_2)$, $R = \max(X_1, X_2) − \min(X_1,X_2)$, and $(X_1 − X_2)$.
This should give you 500 tuples/arrays, each of them constructed using 2 independent
draws. Create a scatter plot of $X_1 − X_2$ versus $\min(X_1, X_2)$.

Hint: use `numpy.random.exponential` to generate random variables following the exponential distribution.
"""
#EMPTYCELL


"""
# GDP

Load the [`datasets/gdp-per-capita-worldbank.csv`](https://ourworldindata.org/grapher/gdp-per-capita-worldbank) dataset.
Plot United States's GDP per capita using a line plot.
"""
#EMPTYCELL


"""
# Democratic Backslash, revisited

Load the [`datasets/electoral-democracy-index.csv`](https://ourworldindata.org/democracy) and [`datasets/population.csv`](https://ourworldindata.org/population-growth) datasets.
For each year (with sufficient data), calculate a population weighted global democracy index.
Plot your data.
What trend do you see? 
"""
df = pd.read_csv("datasets/electoral-democracy-index.csv")
df = df.rename(columns = {
    'Electoral democracy index (best estimate, aggregate: average)': "Democracy"
})
popdf = pd.read_csv("datasets/population.csv")
popdf = popdf.rename(columns = {
    'Population - Sex: all - Age: all - Variant: estimates': "Population"
})
#ANSWER
df = pd.read_csv("datasets/electoral-democracy-index.csv")
df = df.rename(columns = {
    'Electoral democracy index (best estimate, aggregate: average)': "Democracy"
})
popdf = pd.read_csv("datasets/population.csv")
popdf = popdf.rename(columns = {
    'Population - Sex: all - Age: all - Variant: estimates': "Population"
})
#NEWCELL
years = df["Year"].unique()
global_dem_index = {}

for year in years:
    df_year = df[df["Year"] == year].dropna()
    popdf_year = popdf[popdf["Year"] == year].dropna()
    
    common_countries = list(set(df_year["Entity"]) & set(popdf_year["Entity"]))
    
    df_year = df_year.set_index("Entity")
    popdf_year = popdf_year.set_index("Entity")
    
    dem_vec = df_year.loc[common_countries]["Democracy"]
    pop_vec = popdf_year.loc[common_countries]["Population"]
    if len(dem_vec) == 0:
        continue

    global_democracy_index = dem_vec.dot(pop_vec) / pop_vec.sum()
    global_dem_index[year] = global_democracy_index
#NEWCELL
global_dem = pd.DataFrame(global_dem_index, index=["Democracy"]).transpose()
global_dem.plot()



"""
# Save Your Work

Find a way to save your graphs. Do you graphs look blurry? Fix it.

Hint: There are two approaches: (1) increase dpi, (2) store your plot as a vector image. If you want to include you plots into LaTeX files, look into `.pgf` image files.
"""
#EMPTYCELL
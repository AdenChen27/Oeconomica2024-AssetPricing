"""
# Pandas: Data Visualization
"""

"""
# Task 1: Warm up

Install `matplotlib` and use it to plot the following functions:
- $f(x) = x - 1$
- $f(x) = x^7 - x^5$
- $f(x) = \sin(x)$
"""
pass

"""
# Task 2: Democracy of the US

Load the `electoral-democracy-index.csv` file, which contains data on V-Dem's country/year-level democracy index.
- Plot United States data over the years as a line plot.
- Fit a polynomial of degree 4 through the data.
- Clearly label you graph.
"""
pass

"""
# Task 3: A Comparison

Create a new graph, comparing the democracy scores of the US and the UK (plot data of both countries in the same plot).
"""
pass

"""
# Task 4: Probability

(Stolen from Dan Nicolae)

Generate 500 samples of 2 random variables $X_1$ and $X_2$ with distribution $\mathrm{Exponential}(1)$.
For each of the 500 samples, calculate $\min(X_1, X_2)$ $\max(X_1,X_2)$, $R = \max(X_1, X_2) − \min(X_1,X_2)$, and $(X_1 − X_2)$.
This should give you 500 tuples/arrays, each of them constructed using 2 independent
draws. Create a scatter plot of $X_1 − X_2$ versus $\min(X_1, X_2)$.

Hint: use `numpy.random.exponential` to generate random variables following the exponential distribution.
"""
pass


"""
# Task 5: GDP

Load the `gdp-per-capita-worldbank.csv` dataset.
Plot United States's GDP per capita using a line plot.

GDP data taken from World Bank (2023) – with minor processing by Our World in Data.
"""
pass


"""
# Task 6: Save Your Work

Find a way to save your graphs. Do you graphs look blurry? Fix it.

Hint: There are two approaches: (1) increase dpi, (2) store your plot as a vector image. If you want to include you plots into LaTeX files, look into `.pgf` image files.
"""
pass
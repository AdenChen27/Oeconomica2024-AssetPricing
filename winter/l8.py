"""
# Regression Analysis
"""
import numpy as np
import pandas as pd

"""
# Shape
Given a `numpy` array `A`, what does `A.reshape((a, b))` do?

What does `A.reshape((-1, 1))` do? In what way is `A.reshape((-1, 1))` different from `A`?

Hint: one is a matrix, the other a vector.
"""
A = np.array([1, 5, 10, 14, 31, 22, 27, 72])


"""
# `Smoke`

Explore the `smoke` data set from Wooldridge.
Read [this](http://fmwww.bc.edu/ec-p/data/wooldridge/smoke.des).
Produce a scatter plot of smoking behavior and income.
"""
df = pd.read_csv("smoke.csv")


"""
# Simple Regression Analysis

The following code runs a simple regression for `cigs` on `lincome`.
(What does `"\t"` mean?)
"""
from sklearn.linear_model import LinearRegression

model = LinearRegression()
x = df["lincome"].to_numpy().reshape((-1, 1))
y = df["cigs"].to_numpy()
model.fit(x, y)

r_sq = model.score(x, y)

print(f"beta_0:\t{model.intercept_}")
print(f"beta_1:\t{model.coef_}")
print(f"R^2:\t{r_sq}")

"""
You've obtained $\beta_0$ and $\beta_1$ above.
Calculate the predicted value $\hat{y}_i = \beta_0 + \beta_1 x_i$ for each of the entry in `df`.
"""
#EMPTYCELL

"""
Plot the following in the same graph:

- The actual values of smoking vs income. (You have plotted this before. Just reproduce the graph).
- The predicted values of smoking vs income for each entry in `df`.
- The population regression function $E(y | x) = \beta_0 + \beta_1 x$. This should be a straight line.
"""
#EMPTYCELL

"""
### Covariance


The residual $\hat{u}$ is the variation in $y_i$ not captured in our model, given by $\hat{u}_i = y_i - \hat{y}_i$.

- Use to function to calculate, for each entry in `df`, the corresponding residual.
- Calculate the sample covariance between the predicted value $\hat{y}_i = \beta_0 + \beta_1 x_i$ and the error $\hat{u}_i = y_i - \hat{y}_i$. Note its magnitude.

Hint: use [`np.cov`](https://numpy.org/doc/stable/reference/generated/numpy.cov.html). (This function returns a matrix. How does the matrix relate to the covariance?)
"""
#EMPTYCELL


"""
You should obtain 0 (up to any small rounding error). In fact, we always have for any sample that $Cov(\hat{y}_i, \hat{u}_i) = 0$.
The fitted values and the residuals are uncorrelated.
"""
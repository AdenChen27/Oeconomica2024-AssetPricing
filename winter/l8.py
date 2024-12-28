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
You should obtain 0 (up to any small rounding error). In fact, we always have for *any* sample that $Cov(\hat{y}_i, \hat{u}_i) = 0$.
The fitted values and the residuals are uncorrelated.

Moreover, $Cov(\hat{u}_i, f(x_i)) = 0$ for any function $f$.
This is known as the Conditional Expectation Function (CEF) Decomposition property.
"""
"""
The [`statsmodels`](https://www.statsmodels.org/stable/index.html) module provides a much more convenient way to run regressions.
"""
import statsmodels.formula.api as sm
result = sm.ols(formula="cigs ~ lincome", data=df).fit()
result.summary()
"""
The above one line code, for example, runs the simple regression of `cigs` on `lincome` which you've done above.

You can just as easily run multiple regressions, that is, regression on multiple explanatory variables:
"""
result = sm.ols(formula="cigs ~ lincome + age + cigpric + educ", data=df).fit()
result.summary()


"""
# Life Satisfaction

Explore World Happiness Report's [`datasets/WorldHappinessReport2024_DataForTable2.1.csv`](https://worldhappiness.report/data/) dataset on world happiness (measured using the [Cantril ladder](https://news.gallup.com/poll/122453/understanding-gallup-uses-cantril-scale.aspx)).

- Rename the columns (having spaces in names can be extremely annoying, as you may or may not experience if you ignore this step).
    
    You may want to use the following dictionary for renaming.
    ```
    {
        "Country name": "country",
        "Life Ladder": "ladder",
        "Log GDP per capita": "logGDP",
        "Social support": "socialSupport",
        "Healthy life expectancy at birth": "health",
        "Freedom to make life choices": "freedom",
        "Generosity": "generosity",
        "Perceptions of corruption": "corruption",
        "Positive affect": "positiveAffect",
        "Negative affect": "negativeAffect",
    }
    ```
- Let's focus for simplicity on cross-sectional data. To that end, isolate the relevant data in year 2023.

- Regress happiness (`ladder`) on two explanatory variables `logGDP` and `freedom`.

The regression model is:
$$
    \text{ladder} = \beta_0 + \beta_1 \text{logGDP} + \beta_2 \text{health} + u.
$$
What value of $\beta_1$ did you get?
"""
#EMPTYCELL
#ANSWER
df = pd.read_csv("datasets/WorldHappinessReport2024_DataForTable2.1.csv")
df = df.rename(columns={
    "Country name": "country",
    "Life Ladder": "ladder",
    "Log GDP per capita": "logGDP",
    "Social support": "socialSupport",
    "Healthy life expectancy at birth": "health",
    "Freedom to make life choices": "freedom",
    "Generosity": "generosity",
    "Perceptions of corruption": "corruption",
    "Positive affect": "positiveAffect",
    "Negative affect": "negativeAffect",
})
result = sm.ols(formula="ladder ~ logGDP + freedom", data=df).fit()
beta_1 = result.params["logGDP"]
print(beta_1)

"""
Next, regress `logGDP` on `freedom`. The regression model is:
$$
    \text{logGDP} = \gamma_0 + \gamma_1 \text{freedom} + u_2.
$$
- What values of $\gamma_0$ and $\gamma_1$ did you get?

Using $\gamma_0$ and $\gamma_1$, you can obtain estimated values of `logGDP`, `predicted_logGDP` as:
$$
    \text{predicted_logGDP} = \gamma_0 + \gamma_1 \text{freedom}.
$$

- Create thus a new column called `predicted_logGDP` in the DataFrame with the predicted values of logGDP using the values of $\gamma_0$ and $\gamma_1$ you obtained.
"""
#EMPTYCELL
#ANSWER
result = sm.ols(formula="logGDP ~ freedom", data=df).fit()
gamma_0 = result.params["Intercept"]
gamma_1 = result.params["freedom"]

df["predicted_logGDP"] = gamma_1*df["freedom"] + gamma_0

"""
The difference between the predicted value and the true value is called the residual.
$$
    \text{residual} = \text{logGDP} - \text{predicted_logGDP}
$$
- Create a new column called `residual` containing the residuals.
- Run a regression of `ladder` on `residual`.

The regression model is:
$$
    \text{ladder} = \beta_0' + \beta_1' \text{residual} + u_3.
$$
What value of $\beta_1'$ did you get? How does it compare to $\beta_1$?
"""
#EMPTYCELL
#ANSWER
df["residual"] = df["logGDP"] - df["predicted_logGDP"]
result = sm.ols(formula="ladder ~ residual", data=df).fit()
print(result.params["residual"])
"""
This result is known as the Frisch-Waugh-Lovell theorem or the regression anatomy theorem.
"""
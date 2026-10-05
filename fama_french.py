import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from pandas_datareader import data as pdr

def load_factors():
    #download the Fama-French 3-factor data from Kenneth French's website
    ff3 = pdr.DataReader('F-F_Research_Data_Factors', 'famafrench', start='1926-07-01')

    #monthly factor returns are stored in table 0 
    factors = ff3[0]
    
    return factors

#run the function
factors = load_factors()

print(factors.head())
print("\nShape:",factors.shape)
print("\nSummary statistics:")
print(factors.describe())

def load_portfolios():
    """Download monthly 25 Size x Book-to-Market portfolios."""

    data = pdr.DataReader(
        "25_Portfolios_5x5",
        "famafrench",
        start="1926-07-01"
    )

    portfolios = data[0]
    return portfolios

def run_ff3_regression(portfolio_returns, factors):
    """Run a Fama-French 3-factor regression with aligned dates."""

    data = pd.concat(
        [
            portfolio_returns.rename("portfolio"),
            factors[["Mkt-RF", "SMB", "HML", "RF"]]
        ],
        axis=1,
        join="inner"
    ).dropna()

    y = data["portfolio"] - data["RF"]

    X = data[["Mkt-RF", "SMB", "HML"]]
    X = sm.add_constant(X)

    model = sm.OLS(y, X).fit()

    return model

portfolios = load_portfolios()
print("\n25 portfolios:")
print(portfolios.head())
print("\nportfolios shape:", portfolios.shape)

#confirm date range + no missing data 
print("\nFactor dates:", factors.index.min(), "to", factors.index.max())
print("Portfolio dates:", portfolios.index.min(), "to", portfolios.index.max())

print("\nMissing values:")
print("Factors:", factors.isna().sum().sum())
print("Portfolios:", portfolios.isna().sum().sum())

# First Fama-French regression: Small Growth portfolio

# Portfolio excess return
y = portfolios["SMALL LoBM"] - factors["RF"]

# Three Fama-French factors
X = factors[["Mkt-RF", "SMB", "HML"]]

# Add intercept (alpha)
X = sm.add_constant(X)

# Run OLS regression
model = sm.OLS(y, X).fit()

print("\n--- SMALL LoBM: Fama-French 3-Factor Regression ---")
print(model.summary())

# Modern sample: 2010-present

modern_factors = factors.loc["2010-01":]
modern_portfolios = portfolios.loc["2010-01":]

# Excess return for Small Growth portfolio
y_modern = (
    modern_portfolios["SMALL LoBM"]
    - modern_factors["RF"]
)

# Fama-French factors
X_modern = modern_factors[["Mkt-RF", "SMB", "HML"]]
X_modern = sm.add_constant(X_modern)

# Run regression
model_modern = sm.OLS(y_modern, X_modern).fit()

print("\n--- SMALL LoBM: 2010-Present ---")
print(model_modern.summary())

# Run Fama-French 3-factor regressions for all 25 portfolios

results = []

for portfolio in modern_portfolios.columns:

    model = run_ff3_regression(
        modern_portfolios[portfolio],
        modern_factors
    )

    results.append({
        "Portfolio": portfolio,
        "Alpha": model.params["const"],
        "Alpha_t": model.tvalues["const"],
        "Alpha_p": model.pvalues["const"],
        "Beta_Mkt": model.params["Mkt-RF"],
        "Beta_SMB": model.params["SMB"],
        "Beta_HML": model.params["HML"],
        "R2": model.rsquared
    })

results = pd.DataFrame(results)

print("\n=== Fama-French 3-Factor Results: 25 Portfolios ===")
print(results.round(4))


# Factor Regime Lab

### Measuring the stability of equity factor exposures across a century of U.S. market data

Factor models are typically estimated over long historical samples, but the relationships they capture need not remain stable as markets evolve.

**Factor Regime Lab** examines how the explanatory power and estimated exposures of the Fama–French factors change across time and across the 25 Size × Book-to-Market portfolios.

The analysis spans U.S. equity data from 1926 to the present and focuses on three quantities:

- **pricing errors (α)** — returns left unexplained by the model
- **factor exposures (β)** — sensitivity to market, size, and value factors
- **model fit (R²)** — how much return variation the factors explain

The central question is:

> **Are classic equity factor relationships persistent, or are they regime-dependent?**

---

## Research Scope

The analysis is designed around four empirical questions:

1. How stable are market, size, and value exposures through time?
2. Where in the Size × Book-to-Market cross-section does the model produce the largest pricing errors?
3. Has factor behavior changed materially in the post-2010 market?
4. Are apparent changes isolated to individual portfolios or systematic across the cross-section?

---

## Data

Monthly observations are sourced from the **Kenneth R. French Data Library** and extend from July 1926 to the present.

### Factor Returns

| Series | Description |
|---|---|
| Mkt−RF | Market excess return |
| SMB | Small Minus Big — size factor |
| HML | High Minus Low — value factor |
| RF | Risk-free rate |

### Test Assets

The test assets are 25 value-weighted portfolios formed independently on:

- market equity (Size)
- book-to-market equity (B/M)

Together they form a 5 × 5 cross-section ranging from Small/Growth to Big/Value firms.

---

## Empirical Framework

For portfolio *i*, monthly excess returns are estimated using the Fama–French three-factor model:

$$
R_{i,t} - R_{f,t}
=
\alpha_i
+ \beta_{MKT,i}(R_{M,t} - R_{f,t})
+ \beta_{SMB,i}SMB_t
+ \beta_{HML,i}HML_t
+ \epsilon_{i,t}
$$

The analysis extracts three sets of diagnostics from each regression:

**Pricing error**
- α
- t-statistic
- statistical significance

**Factor structure**
- βMKT
- βSMB
- βHML

**Explanatory power**
- R²

These quantities are evaluated across portfolios and across time rather than interpreted as fixed characteristics.

---

## Analytical Pipeline

The current pipeline:

1. retrieves monthly factor and portfolio returns
2. aligns observations by date
3. constructs portfolio excess returns
4. estimates factor models across the 25 test assets
5. extracts coefficients, inference statistics, and model fit
6. compares long-run estimates with the post-2010 sample

The next analytical layer will introduce rolling estimation and regime-level comparisons to measure parameter stability directly.

---

## Research Roadmap

### Cross-sectional diagnostics
- 5 × 5 alpha maps
- factor-loading maps
- significance patterns
- comparison of model fit across test assets

### Temporal stability
- historical vs. modern estimates
- rolling factor loadings
- rolling pricing errors
- rolling R²

### Robustness
- heteroskedasticity/autocorrelation-robust inference
- alternative sample definitions
- joint tests of pricing errors
- comparison with expanded factor specifications

---

## Repository

```text
ff-factor/
├── fama_french.py
├── README.md
├── requirements.txt
└── .gitignore
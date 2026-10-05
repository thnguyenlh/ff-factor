# Fama–French Three-Factor Model: A Modern Reassessment

## Overview

This project examines the Fama–French Three-Factor Model using U.S. equity portfolio data from Kenneth French's Data Library.

The analysis asks a simple question:

> How well does the classic Fama–French Three-Factor Model explain the cross-section of stock returns, and has its explanatory power changed in the modern market?

Rather than treating the model as a historical result, this project compares its performance across different time periods, with particular attention to the post-2010 market.

## Model

The Fama–French Three-Factor Model is estimated as:

Rᵢ,t − RFₜ = αᵢ + βMKT(MKTₜ − RFₜ) + βSMB SMBₜ + βHML HMLₜ + εᵢ,t

where:

- **MKT − RF**: market excess return
- **SMB**: size factor (Small Minus Big)
- **HML**: value factor (High Minus Low)
- **α**: abnormal return not explained by the three factors

## Data

Data are obtained from the Kenneth R. French Data Library.

The project uses:

- Monthly Fama–French three-factor returns
- 25 portfolios sorted by Size and Book-to-Market
- Historical sample beginning in 1926
- Modern subsample beginning in 2010

Using the 25 Size × Book-to-Market portfolios allows the model to be tested across firms with systematically different size and value characteristics.

## Methodology

The project estimates time-series OLS regressions for each of the 25 portfolios.

The analysis compares:

1. Full historical sample
2. Modern market period (2010–present)
3. Factor loadings across portfolio characteristics
4. Portfolio-level pricing errors (alpha)
5. Model explanatory power (R²)

The goal is not only to reproduce the classic Fama–French regression, but to examine where the model continues to perform well and where its explanatory power may weaken in more recent markets.

## Current Progress

- [x] Download Fama–French factor data
- [x] Download 25 Size × Book-to-Market portfolios
- [x] Align portfolio and factor dates
- [x] Estimate initial three-factor regression
- [x] Create modern 2010–present sample
- [x] Build reusable regression function
- [ ] Estimate all 25 portfolio regressions
- [ ] Analyze alpha patterns
- [ ] Compare historical and modern results
- [ ] Visualize factor loadings
- [ ] Test joint pricing errors
- [ ] Document findings

## Tools

- Python
- pandas
- NumPy
- statsmodels
- matplotlib
- pandas-datareader

## Research Questions

This project focuses on three questions:

1. How effectively does the Fama–French Three-Factor Model explain returns across the 25 Size × Book-to-Market portfolios?
2. Does model performance differ between the historical sample and the post-2010 period?
3. Which types of portfolios produce the largest unexplained returns?

## Status

Work in progress.
---
name: research-descriptive-statistics
description: >-
  Summarize data correctly: central tendency, dispersion, distribution shape, when mean vs median, outlier handling, the right chart — use before any inferential test
---

# research-descriptive-statistics

Always describe before you infer. Report central tendency AND dispersion together: **mean + SD** only for roughly symmetric data; **median + IQR** for skewed data or ordinal scales (income, response times, Likert). Check shape first with a histogram and boxplot — the mean of right-skewed income data is a lie about the typical case.

Quantify shape: skewness (sign = tail direction) and kurtosis. Flag outliers with the 1.5*IQR rule or |z| > 3, but investigate before deleting — an outlier may be the finding, not noise. Use the **coefficient of variation** (SD/mean) to compare dispersion across variables on different scales.

For categorical data, report frequencies and proportions, not means. For grouped comparisons, a table of n, mean/median, SD/IQR per group is the standard "Table 1". In Python, `df.describe()` plus `df.groupby(...).agg(...)` and seaborn boxplots; in R, `summary()` + `psych::describe()`.

Pitfall: reporting a mean for ordinal Likert items as if the spacing between points is equal. Second pitfall: bar charts of means with no error bars — always show variability (SD, SE, or CI), and say which one.

**Tools:** mean/median/mode, SD/IQR, skewness/kurtosis, boxplot/histogram, z-score, pandas describe(), coefficient of variation

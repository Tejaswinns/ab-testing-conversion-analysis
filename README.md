# A/B Testing Conversion Analysis

## Overview
This project performs a comprehensive A/B testing analysis on conversion data, comparing the performance of a control group (old page) versus a treatment group (new page).

## Business Question
Does changing the webpage from the control version to the treatment
version lead to a meaningful difference in user conversion?

## Hypotheses
**H0:** There is no significant difference in conversion rates
between the control and treatment groups.

**H1:** There is a significant difference in conversion rates
between the control and treatment groups.

## Analytical Workflow
1. Load and inspect the dataset
2. Check data quality and group distributions
3. Calculate control and treatment conversion rates
4. Measure conversion uplift
5. Perform hypothesis testing
6. Visualize conversion-rate differences
7. Build and evaluate the logistic regression model
8. Interpret the results and draw conclusions
   
## Dataset
- **Total Users:** 290,584
- **Control Group:** 145,232 users
- **Treatment Group:** 145,352 users
- **Date Range:** 2017-01-02 to 2017-01-24

## Key Findings
- **Control Conversion Rate:** 12.04%
- **Treatment Conversion Rate:** 11.89%
- **Conversion Uplift:** -0.15%
- **P-value:** 0.216 (Not Statistically Significant)
- **Model Accuracy:** 88.13%

## Conclusion
There is **no statistically significant difference** between the control and treatment groups at the 0.05 significance level. The treatment page does not perform meaningfully different from the control page.

## Methods Used

### 1. A/B Testing Statistical Analysis
- Quantitative comparison of conversion rates between control and treatment groups
- Segmentation and aggregation of user behavior by group

### 2. Hypothesis Testing (t-test)
- Two-sample t-test to compare mean conversion rates
- Tests the null hypothesis that both groups have equal conversion rates
- P-value interpretation for statistical significance

### 3. Logistic Regression Model
- Binary classification model to predict conversion probability
- Features: group (control/treatment) encoded as numeric variable
- Training and testing on 80/20 split
- Model evaluation using accuracy metric

### 4. Data Visualization
- Bar plots comparing conversion rates by group
- Conversion count distributions
- Group size comparisons
- Visual representation saved as PNG for easy interpretation

## Project Structure
```
ab-testing-conversion-analysis/
├── Data/
│   └── ab_data.csv/
│       └── ab_data.csv
├── src/
│   └── analysis.py
├── results/
│   ├── analysis_report.txt
│   └── conversion_rate_plot.png
├── requirements.txt
└── README.md
```

## Installation
1. Install required dependencies:
```bash
pip install -r requirements.txt
```

2. Ensure you have Python 3.8+ installed

## Usage
Run the analysis script:
```bash
python src/analysis.py
```

This will generate:
- `results/analysis_report.txt` - Detailed analysis report
- `results/conversion_rate_plot.png` - Visualization charts

## Dependencies
- pandas - Data manipulation and analysis
- numpy - Numerical computations
- matplotlib - Data visualization
- seaborn - Statistical visualization
- scipy - Statistical testing
- scikit-learn - Machine learning models

## Author
A/B Testing Analysis Project

## License
MIT

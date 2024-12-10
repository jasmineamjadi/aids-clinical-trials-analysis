# AIDs Treatment Effectiveness: Monotherapy vs. Combination Therapy

## Introduction

This project evaluates the effectiveness of monotherapeutic vs. combination AIDs treatments using clinical trial data. Specifically, it examines the proportion of failure outcomes associated with:

- **Zidovudine (ZDV)**
- **Didanosine (ddI)**
- **ZDV + Zalcitabine (Zal)**
- **ZDV + ddI**

The goals of this analysis are:
1. To identify the treatment and therapy type with the lowest proportion of failure outcomes.
2. To determine if combination therapies reduce failure events compared to monotherapies.

## Table of Contents

1. [Introduction](#introduction)
2. [Dataset](#dataset)
3. [Methods](#methods)
   - [Data Preprocessing](#data-preprocessing)
   - [Analysis and Visualization](#analysis-and-visualization)
4. [Dependencies](#dependencies)
5. [License](#license)

## Dataset

The dataset used in this project was obtained from Kaggle: [AIDS Clinical Trials Dataset](https://www.kaggle.com/datasets/tanshihjen/aids-clinical-trials).

This dataset provides information on clinical trials investigating various monotherapeutic and combination therapies for HIV/AIDS treatment.

## Methods
### Data Preprocessing

The preprocessing steps involve:
- Loading raw clinical trial data.
- Cleaning and formatting the dataset for analysis.
- Handling outliers to ensure robust results.
- Saving the processed data for downstream analysis.

The preprocessing steps are implemented in the notebook `1_preprocessing.ipynb`, and the cleaned dataset is stored as `aids_clinical_trials_cleaned.csv`.

### Analysis and Visualization

The analysis focuses on the following:

1. **Hypotheses Testing**:
   - **Null Hypothesis (H₀):** The proportion of failure events is the same between monotherapy and combination therapies.
   - **Alternative Hypothesis (Hᴀ):** There is a significant difference in the proportion of failure events between monotherapy and combination therapies.

2. **Statistical Analysis**:
   - A Chi-Square test is performed to evaluate the relationship between therapy types and failure events.

3. **Visualization**:
   -  A graphical representation is used to illustrate differences in treatment outcomes across the therapies.

These analyses are implemented in the notebook `2_treatment_effectiveness.ipynb`.

## Dependencies

This project uses the following libraries and tools:
- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `scipy`
- `IPython` (for Markdown display in Jupyter notebooks)

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.

# Sleep Study Data Analysis

## Overview
This repository contains an in-depth analysis of a sleep study dataset. The data was collected from a survey-based study on the sleeping habits of individuals within the US.

## Purpose
The analysis aims to explore various factors influencing sleep duration and quality, investigating relationships between sleep patterns and different lifestyle choices such as breakfast consumption, phone usage, tiredness levels, etc.

## Methodology
The analysis includes:
- Data cleaning and preprocessing
- Exploratory data analysis (EDA) to visualize and understand data distributions
- Statistical analysis to test hypotheses regarding factors affecting sleep patterns
- Visualization of interactions between various factors affecting sleep

## Files
- `demo_categorical_sleep.ipynb`: Jupyter Notebook containing the complete analysis workflow
- `config.yaml`: Configuration file with data file path and image references
- `stats_functions.py`: Module containing custom statistical functions used in the analysis
- `sleep.csv`: Dataset used for analysis (not included in this repository)

## Analysis Details
- Data Inspection: Examining dataset structure, missing values, and data types
- Visualization: Utilizing histograms, bar plots, and box plots for data exploration
- Statistical Tests: Applying Mann-Whitney U, Kruskal-Wallis, and ANOVA tests to assess factor impacts on sleep patterns
- Undersampling: Balancing the dataset to observe effects on statistical significance

## Conclusion
The analysis reveals significant correlations between specific lifestyle choices (e.g., breakfast consumption, phone usage) and sleep duration. However, while interactions between certain factors show promise, statistical significance remains uncertain due to dataset limitations.

## How to Use
1. Clone the repository.
2. Ensure required dependencies are installed (see requirements.txt)
3. Execute `demo_categorical_sleep.ipynb` in a Jupyter Notebook environment.

NB. This readme is partly generated with chatgtp 3.5

## Author
F. Feenstra f.feenstra@pl.hanze.nl
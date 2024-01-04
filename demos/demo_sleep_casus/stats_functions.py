
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import shapiro
from statsmodels.graphics.gofplots import qqplot
from scipy.stats import norm
from scipy.stats import mannwhitneyu, kruskal, f_oneway
from statsmodels.formula.api import ols
import statsmodels.api as sm 

def assess_normality(data):
    """
    Test the normality of a given dataset using Shapiro-Wilk test and Q-Q plot.

    Args:
        data (array-like): The dataset to be assessed for normality.

    Returns:
        None
    """
    qqplot(data,norm,fit=True,line="45")
    plt.show()
    # Calculate Shapiro-Wilk test
    alpha = 0.05  
    statistic, p_value = shapiro(data)

    # Print the test result
    print("HO: data follows normal distribution")
    print("H1: data does not follow normal distribution")
    print(f"Shapiro-Wilk test statistic: {statistic:.3f} and p-value: {p_value:.2e}")

    # Interpret the p-value
    if p_value > alpha:
        print(f"The data is normally distributed (do not reject H0) with alpha = {alpha}")
    else:
       print(f"The data is not normally distributed (reject H0) with alpha = {alpha}")


def Mann_Whitney_U(df,column, dependent='Hours'):
    """ function that executes Mann Witney U test and prints results

    Args:
        df (pandas dataframe): pandas dataframe to be used
        column (str): pandas dataframe column name to group by
    
    Returns:
        None
    """
    group1=df[df[column]=='Yes'][dependent]
    group2=df[df[column]=='No'][dependent]
    print(f"\nMann Whitney U test for hours of sleep grouped by {column}")
    statistic, p_value = mannwhitneyu(group1, group2)
    print(f"U Statistic: {statistic}")
    print(f"P-value: {p_value}")

    alpha = 0.05  
    if p_value < alpha:
        print(f"The difference between the groups by {column} is statistically significant")
    else:
        print(f"The difference between the groups by {column} is not statistically significant")
 

def kruskalt(df,columns, dependent='Hours'):
    """ function that executes Kruskall-Wallis test and prints results

    Args:
        df (pandas dataframe): pandas dataframe to be used
        columns (array-like): list of pandas dataframe column names to group by
        dependent(str): dependent variable
    
    Returns:
        None
    """
    print(f'\nKruskal-Wallis test for hours of sleep grouped by {columns}')
    grouped = df.groupby(columns)[dependent]
    grouped_data = {key:np.array(group) for key, group in grouped}
    statistic, p_value = kruskal(*grouped_data.values())
    print(f"U Statistic: {statistic}")
    print(f"P-value: {p_value}")
    alpha = 0.05  
    if p_value < alpha:
        print(f"The difference between the groups by {columns} is statistically significant")
    else:
        print(f"The difference between the groups by {columns} is not statistically significant")
 

def anova_test(df,columns,dependent='Hours'):
    """ function that executes one way and two way anova and prints results

    Args:
        df (pandas dataframe): pandas dataframe to be used
        columns (list): list of pandas dataframe column names to group by
        dependent(str): dependent variable
    
    Returns:
        None
    """
    # Perform one-way ANOVA for Breakfast 
    statistic, p_value = f_oneway(df[dependent][df[columns[0]] == "Yes"],
                                  df[dependent][df[columns[0]] == "No"])
    print(f"one-way Statistic: {statistic:.3f}")
    print(f"P-value: {p_value:.3f}")

    alpha = 0.05  
    if p_value < alpha:
        print(f"The difference between the groups by {columns[0]} is statistically significant")
    else:
        print(f"The difference between the groups by {columns[0]} is not statistically significant")
 
    # Perform two-way ANOVA for research question 2
    if len(columns)==2:
        formula = f'{dependent} ~ C({columns[0]}) + C({columns[1]}) + C({columns[0]})*C({columns[1]})'
        model = ols(formula, data=df).fit()
        two_way = sm.stats.anova_lm(model, typ=2)
        print(f"\nTwo-way ANOVA for {dependent} by {columns[0]} and {columns[1]} is:\n{two_way}\n")
    if len(columns)==3:
        formula = f'{dependent} ~ C({columns[0]}) + C({columns[1]}) + C({columns[2]})'
        formula += f'+ C({columns[0]})*C({columns[1]}) + C({columns[1]})*C({columns[2]})'
        formula += f'+ C({columns[0]})*C({columns[2]})'
        formula += f'+ C({columns[0]}):C({columns[1]}):C({columns[2]})'
        model = ols(formula, data=df).fit()
        two_way = sm.stats.anova_lm(model)
        print(f"\nTwo-way ANOVA for {dependent} by {columns} is:\n{two_way}\n")
      

    
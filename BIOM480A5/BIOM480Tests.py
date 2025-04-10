# This file is part of the BIOM480A5 course discussion. 
# Each student will present on a different topic related to statistical tests.
# The goal is to create a function for each topic that can be used to perform the test.
# Each student will create a function with the following format:
# def function_name(parameters):
#     '''
#     Description of the function and its parameters.
#     Parameters:
#     parameter1 : type
#         Description of parameter1.
#     parameter2 : type
#         Description of parameter2.
#     Returns:
#     return_value : type
#         Description of return_value.
#     Example:
#     >>> function_name(parameter1, parameter2)
#     >>> print(return_value)
#     Notes:
#     Additional notes about the function.
#     '''
# The function should be able to be called from the command line or from another script.

# Please enter your tests below in the correct location (look for your name). 
# If you need to add a module, please do so at the top.

import numpy as np
from scipy import stats

# Example will present on the topic of t-test, creating function named 'ttest'
def ttest(a, b):
    '''
    Perform a t-test on two independent samples.
    Parameters:
    a : array_like
        First sample.
    b : array_like
        Second sample.
    Returns:
    t_stat : float
        The calculated t-statistic.
    p_value : float
        The two-tailed p-value.

    Example:
    >>> a = [1, 2, 3, 4, 5]
    >>> b = [2, 3, 4, 5, 6]
    >>> t_stat, p_value = ttest(a, b)
    >>> print(t_stat)
    0.0
    >>> print(p_value)
    0.3465935070873343
    
    Notes:
    This function assumes that the two samples have equal variances.
    The p-value is calculated using the two-tailed test.
    '''
    # Calculate the means and standard deviations
    mean_a = np.mean(a)
    mean_b = np.mean(b)
    std_a = np.std(a, ddof=1)
    std_b = np.std(b, ddof=1)
    n_a = len(a)
    n_b = len(b)
    # Calculate the t-statistic
    t_stat = (mean_a - mean_b) / np.sqrt((std_a**2 / n_a) + (std_b**2 / n_b))
    # Calculate the degrees of freedom
    df = n_a + n_b - 2
    # Calculate the p-value
    p_value = 2 * (1 - np.abs(t_stat) / np.sqrt(df))
    return t_stat, p_value

#*********************


# Becca B will present on the topic of Breusch-Pagan test, creating function named 'breusch_pagan' 

#*********************
# Ella B will present on the topic of Variance Inflation Factor (VIF) test, creating function named 'vif' 

#*********************
# Lauren B will present on the topic of Jarque-Bera test, creating function named 'jarque_bera' 

#*********************
# James B will present on the topic of Hotelling’s T-squared test, creating function named 'hotelling_t' 

#*********************
# Chayanee C will present on the topic of D’Agostino and Pearson’s test, creating function named 'dagostino' 
import numpy as np
from scipy.stats import skew, kurtosis, skewtest, kurtosistest, normaltest

def dagostino(data):
    '''
    Perform D'Agostino and Pearson's test for normality and return detailed diagnostics.

    Parameters:
    data : array_like
        A one-dimensional array of sample data.

    Returns:
    results : dict
        Dictionary containing:
        - 'k2_statistic': combined test statistic
        - 'p_value': p-value of the test
        - 'skewness': sample skewness
        - 'kurtosis': sample excess kurtosis
        - 'z_skew': skewness Z-score
        - 'z_kurt': kurtosis Z-score

    Example:
    >>> data = [-1.83, -0.58, 0.70, -1.35, 0.89, -0.18, 2.88, 0.94, -0.43, 0.27]
    >>> result = dagostino(data)
    >>> for key, val in result.items():
            print(f"{key}: {val:.4f}")

    Notes:
    This function evaluates both skewness and kurtosis to test for normality using the 
    D'Agostino and Pearson test. It provides individual shape measures as well 
    as the combined test statistic and p-value.
    '''
    # Calculate skewness and kurtosis
    skew_val = skew(data)
    kurt_val = kurtosis(data)  # excess kurtosis by default

    # Get Z-scores for skewness and kurtosis
    z_skew, _ = skewtest(data)
    z_kurt, _ = kurtosistest(data)

    # Combined K² test
    k2_stat, p_value = normaltest(data)

    # Return all results as a dictionary
    return {
        'K2_statistic': k2_stat,
        'p_value': p_value,
        'Skewness': skew_val,
        'Excess Kurtosis': kurt_val,
        'Z-score (skewness)': z_skew,
        'Z-score (kurtosis)': z_kurt
    }

#*********************
# Deven D will present on the topic of Chi-square goodness-of-fit test, creating function named 'chi2gof' 
def chi2gof(observed, expected=None, p_vals=None, ddof=0):
    '''
    Perform a chi-square goodness-of-fit test.
    
    Parameters:
    observed : array_like
        Observed frequencies in each category.
    expected : array_like, optional
        Expected frequencies in each category. If None, a uniform distribution is assumed.
    p_vals : array_like, optional
        Probability for each category under null hypothesis. If provided, expected is calculated as p_vals * sum(observed).
    ddof : int, optional
        Delta degrees of freedom. Number of parameters estimated to calculate the expected frequencies.
        
    Returns:
    chi2_stat : float
        The chi-square test statistic.
    p_value : float
        The p-value for the test.
    
    Example:
    >>> observed = [16, 18, 16, 14, 12, 12]  # Observed frequencies of die rolls
    >>> p_vals = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]  # Expected probabilities for fair die
    >>> chi2_stat, p_value = chi2gof(observed, p_vals=p_vals)
    >>> print(f"Chi-square statistic: {chi2_stat:.4f}")
    Chi-square statistic: 2.0000
    >>> print(f"p-value: {p_value:.4f}")
    p-value: 0.8491
    
    Notes:
    - For the test to be valid, each expected frequency should typically be at least 5.
    - The null hypothesis is that the observed frequencies match the expected frequencies.
    - A low p-value suggests rejecting the null hypothesis, indicating the data doesn't fit the expected distribution.
    '''
    # Convert to numpy arrays for easier manipulation
    observed = np.asarray(observed)
    
    # Calculate expected frequencies if not provided
    if expected is None:
        if p_vals is not None:
            p_vals = np.asarray(p_vals)
            if not np.isclose(np.sum(p_vals), 1.0):
                raise ValueError("Probabilities must sum to 1")
            expected = p_vals * np.sum(observed)
        else:
            # Uniform distribution if neither expected nor p_vals provided
            expected = np.ones_like(observed) * np.sum(observed) / len(observed)
    else:
        expected = np.asarray(expected)
    
    # Check that observed and expected have the same shape
    if observed.shape != expected.shape:
        raise ValueError("Observed and expected arrays must have the same shape")
    
    # Check that all expected frequencies are > 0
    if np.any(expected <= 0):
        raise ValueError("All expected frequencies must be positive")
    
    # Calculate chi-square statistic
    chi2_stat = np.sum(((observed - expected) ** 2) / expected)
    
    # Calculate degrees of freedom
    df = len(observed) - 1 - ddof
    
    # Calculate p-value
    p_value = 1 - stats.chi2.cdf(chi2_stat, df)
    
    return chi2_stat, p_value
#*********************
# Jackson E will present on the topic of McNemar’s test, creating function named 'mcnemar' 

#*********************
# Delaney E will present on the topic of Ramsey RESET test, creating function named 'reset_test' 

# The Ramsey RESET test is used to check for model misspecification in regression analysis.
import statsmodels.api as sm
import pandas as pd

def reset_test(model, degree=2):
    '''
    Performs the Ramsey RESET test for model specification.

    Parameters:
    model : statsmodels.regression.linear_model.RegressionResultsWrapper
        A fitted OLS model from statsmodels.
    degree : int
        The maximum power of the fitted values to include in the test (e.g., 2 includes yhat^2, 3 includes yhat^3, etc.).

    Returns:
    reset_result : dict
        A dictionary containing the F-statistic, p-value, and null hypothesis statement.

    Example:
    >>> import statsmodels.api as sm
    >>> import pandas as pd
    >>> from sklearn.datasets import load_iris

    >>> # Load the Iris dataset
    >>> data = load_iris()
    >>> df = pd.DataFrame(data.data, columns=data.feature_names)
    >>> df['species'] = data.target

    >>> # Define independent and dependent variables
    >>> X = df[['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']]
    >>> X = sm.add_constant(X)  # add intercept
    >>> y = df['species']  # species as dependent variable

    >>> # Fit the initial linear regression model
    >>> model = sm.OLS(y, X).fit()

    >>> # Call the Ramsey RESET test with the degree argument
    >>> result = reset_test(model, degree=3)

    >>> # Print the test result
    >>> print("Ramsey RESET Test Result:")
    >>> for key, value in result.items():
    >>>     print(f"{key}: {value}")
    
    Ramsey RESET Test Result:
    F-statistic: <value>
    p-value: <value>
    df_diff: <value>
    Null Hypothesis: Model is correctly specified. (No omitted nonlinear terms)

    Notes:
    The Ramsey RESET test detects general misspecification in a linear regression model
    by adding powers of the fitted values and testing their joint significance.
    A low p-value suggests the model may be missing nonlinear components.
    '''
    
    # Check if the model is fitted/get fitted values
    yhat = model.fittedvalues
    # Create new dataframe with powers of fitted values
    df = model.model.exog.copy()
    for d in range(2, degree + 1):
        df = pd.DataFrame(df, columns=model.model.exog_names)  # Convert to DataFrame to append new columns
        # Add new columns for each power of fitted values
        df[f'yhat^{d}'] = yhat**d

    # Fit a new model with the original predictors and the new polynomial terms
    y = model.model.endog
    new_model = sm.OLS(y, sm.add_constant(df)).fit()

    # Perform the F-test for the new model against the original model
    f_test = new_model.compare_f_test(model)

    # Extract the F-statistic and p-value
    reset_result = {
        'F-statistic': f_test[0],
        'p-value': f_test[1],
        'df_diff': int(f_test[2]),
        'Null Hypothesis': 'Model is correctly specified. (No omitted nonlinear terms)'
    }

    return reset_result

#*********************
# Christian F will present on the topic of Shapiro-Wilk test, creating function named 'shapiro' 

#*********************
# Lillian G will present on the topic of Mantel test, creating function named 'mantel' 

#*********************
# Andy G will present on the topic of Permutation test, creating function named 'permutation_test' 

#*********************
# Emma G will present on the topic of Anderson-Darling test, creating function named 'anderson' 

#*********************
# Nick G will present on the topic of Boschloo’s test, creating function named 'boschloo' 

#*********************
# Joshua H will present on the topic of Cochran’s Q test, creating function named 'cochran_q' 

#*********************
# Paycen H will present on the topic of Phi coefficient test, creating function named 'phicoeff' 

#*********************
# Kyle H will present on the topic of Fisher’s exact test, creating function named 'fisher_exact' 
def fisher_exact(table):
    '''
    Performs Fisher's exact test for a 2x2 contingency table.
    
    Parameters:
    table : array-like
        A 2x2 contingency table in the form of a list of lists or numpy array
        [[a, b], [c, d]] where:
        a = number of successes in group 1
        b = number of successes in group 2
        c = number of failures in group 1
        d = number of failures in group 2
    
    Returns:
    p_value : float
        The p-value from Fisher's exact test
    
    Example:
    >>> table = [[8, 2], [1, 5]]  # Treatment vs. Control recovery data
    >>> p_value = fisher_exact(table)
    >>> print(p_value)
    0.0350877192982456
    
    Notes:
    This function calculates the exact probability of observing the given table
    or one more extreme under the null hypothesis of independence.
    It is particularly useful for small sample sizes where chi-square 
    approximations may not be valid.
    '''
    import numpy as np
    from scipy import stats
    
    # Convert input to numpy array if it's not already
    table = np.array(table, dtype=np.int64)
    
    # Check if the table is 2x2
    if table.shape != (2, 2):
        raise ValueError("Fisher's exact test requires a 2x2 contingency table")
    
    # Perform Fisher's exact test using SciPy
    odds_ratio, p_value = stats.fisher_exact(table)
    
    return p_value

#*********************
# Emma H will present on the topic of Spearman correlation test, creating function named 'spearmanr' 
def spearmanr(x, y):

    '''
    Perform a Spearman rank-order correlation test.
    Parameters:
    x : array_like
        First sample.
    y : array_like
        Second sample.
    Returns:
    correlation : float
        The Spearman correlation.
    p_value : float
        The two-tailed p-value.

    Example:
    >>> x = [1, 2, 3, 4, 5]
    >>> y = [2, 3, 4, 5, 6]
    >>> correlation, p_value = spearmanr(x, y)
    >>> print(correlation)
    1.0
    >>> print(p_value)
    0.0
    
    Notes:
    This function calculates the Spearman rank-order correlation coefficient and its p-value.
    The p-value is calculated using the two-tailed test.
    The function assumes that the input data is one-dimensional and of equal length.
    '''

    # Calculate the ranks of the data
    ranks_x = stats.rankdata(x)
    ranks_y = stats.rankdata(y)
    # Calculate the Spearman correlation
    correlation = np.corrcoef(ranks_x, ranks_y)[0, 1]
    # Calculate the p-value
    n = len(x)
    t_stat = correlation * np.sqrt((n - 2) / (1 - correlation**2))
    p_value = 2 * (1 - stats.t.cdf(np.abs(t_stat), df=n - 2))
    return correlation, p_value
#*********************
# Elijah J will present on the topic of Bartlett’s test, creating function named 'bartlett' 

#*********************
# Gabriela J will present on the topic of Chi-square test of independence, creating function named 'chi2indep' 

#*********************
# Addison L will present on the topic of Permutation test for correlation, creating function named 'permutation_corr' 

#*********************
# Matthew L will present on the topic of Lilliefors test, creating function named 'lilliefors' 

#*********************
# Hassan M will present on the topic of Partial correlation test, creating function named 'partial_corr' 

#*********************
# Bella P will present on the topic of Durbin-Watson test, creating function named 'durbin_watson' 

#*********************
# Chris RT will present on the topic of Fligner-Killeen test, creating function named 'fligner_killeen' 

#*********************
# Mariana S will present on the topic of Point-Biserial correlation test, creating function named 'pointbiserialr' 

#*********************
# Dylan S will present on the topic of Barnard’s exact test, creating function named 'barnard_exact' 

#*********************
# Jacob S will present on the topic of Pearson correlation test, crating function named 'pearsonr' 

#*********************
# Hayley S will present on the topic of Brown-Forsythe test, creating function named 'brown_forsythe' 

#*********************
# Kayla T will present on the topic of Distance correlation test, creating function named 'dcor' 

#*********************
# Vivia VDM will present on the topic of White test, creating function named 'white_test' 

#*********************
# Fig V will present on the topic of Linear regression coefficient test, creating function named 'linreg' 

#*********************
# AbbyMae W will present on the topic of Kendall’s Tau correlation test, creating function named 'kendalltau' 
import numpy as np
from scipy import stats
def kendalltau(x, y):
    '''
    This function calculates the Kendall's Tau correlation coefficient and its p-value.
    
    Parameters:
    x : First array
    y : Second array 
       
    Returns:
    tau : float
        The calculated Kendall's Tau statistic.
    p_value : float
        The two-tailed p-value.
    '''
    tau, p_value = stats.kendalltau(x, y)
    return tau, p_value
#*********************
# Alvina Y will present on the topic of F-test for overall regression, creating function named 'f_test' 

#*********************
# Polina Z will present on the topic of Harvey-Collier test, creating function named 'harvey_collier'

#*********************


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

#*********************
# Deven D will present on the topic of Chi-square goodness-of-fit test, creating function named 'chi2gof' 

#*********************
# Jackson E will present on the topic of McNemar’s test, creating function named 'mcnemar' 

#*********************
# Delaney E will present on the topic of Ramsey RESET test, creating function named 'reset_test' 

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
def boschloo(table, alternative='two-sided'):
    '''
    Perform Boschloo's exact test on a 2x2 contingency table.
    
    Boschloo's test is a more powerful alternative to Fisher's exact test for 2x2 contingency tables.
    It uses Fisher's p-value as a test statistic and finds the probability of obtaining
    a test statistic at least as extreme as the observed one.
    
    Parameters:
    -----------
    table : array_like
        A 2x2 contingency table. Elements should be non-negative integers.
        The table should be in the format:
            [[a, b], [c, d]]
        where a, b, c, d are the cell counts.
    
    alternative : {'two-sided', 'less', 'greater'}, optional
        Defines the alternative hypothesis. Default is 'two-sided'.
        - 'two-sided': the odds ratio of the underlying population is not one
        - 'less': the odds ratio of the underlying population is less than one
        - 'greater': the odds ratio of the underlying population is greater than one
    
    Returns:
    --------
    statistic : float
        The calculated test statistic - in this case, the p-value from Fisher's exact test.
    
    p_value : float
        The p-value for the Boschloo test, representing the probability of obtaining
        a distribution at least as extreme as the observed one, assuming the null
        hypothesis is true.
    
    Example:
    --------
    >>> table = [[74, 31], [43, 32]]
    >>> statistic, p_value = boschloo(table, alternative="greater")
    >>> print(statistic)
    0.0483  # This is the Fisher's p-value
    >>> print(p_value)
    0.0355  # This is the Boschloo's p-value
    
    Notes:
    ------
    - This function relies on scipy.stats.fisher_exact to calculate the Fisher's exact test p-value
    - Boschloo's test is appropriate when the row sums are fixed but the column sums are not
    - Unlike Fisher's test, Boschloo's test is not symmetric: transposing the table will generally
      give different results
    - Boschloo's test is uniformly more powerful than Fisher's exact test
    '''
    import numpy as np
    from scipy import stats
    
    # Convert input to numpy array
    table = np.asarray(table, dtype=np.int64)
    
    # Check dimensions
    if table.shape != (2, 2):
        raise ValueError("The input table must be a 2x2 contingency table")
    
    # Check for negative values
    if np.any(table < 0):
        raise ValueError("All elements in the table must be non-negative")
    
    # Extract values from the table
    a, b = table[0]
    c, d = table[1]
    
    # Get row and column sums
    row_sums = np.sum(table, axis=1)  # [a+b, c+d]
    col_sums = np.sum(table, axis=0)  # [a+c, b+d]
    n = np.sum(table)  # a+b+c+d
    
    # Calculate the test statistic (Fisher's exact p-value)
    _, fisher_p = stats.fisher_exact(table, alternative=alternative)
    statistic = fisher_p  # The statistic is Fisher's p-value
    
    # Generate all possible tables with the same row sums
    def generate_possible_tables():
        tables = []
        # Maximum possible value for a is min(row_sum[0], col_sum[0])
        max_a = min(row_sums[0], col_sums[0])
        
        for i in range(max_a + 1):
            new_a = i
            new_b = row_sums[0] - new_a
            new_c = col_sums[0] - new_a
            new_d = row_sums[1] - new_c
            
            # Check if the table is valid (all entries should be non-negative)
            if new_b >= 0 and new_c >= 0 and new_d >= 0:
                tables.append(np.array([[new_a, new_b], [new_c, new_d]]))
        
        return tables
    
    # Calculate the p-values for all possible tables
    observed_fisher_p = statistic
    possible_tables = generate_possible_tables()
    
    # Calculate probabilities of each possible table under the null hypothesis
    # We use the maximum likelihood estimate of the common binomial parameter
    # which is (a + c) / (a + b + c + d) under H0: p1 = p2
    p_common = col_sums[0] / n
    
    table_probs = []
    for table in possible_tables:
        a_t, b_t = table[0]
        c_t, d_t = table[1]
        
        # Calculate probability of this table using binomial distributions
        # Pr(table) = Pr(a | n1, p) * Pr(c | n2, p)
        # where n1 = a+b, n2 = c+d, p = (a+c)/(a+b+c+d)
        prob_a = stats.binom.pmf(a_t, row_sums[0], p_common)
        prob_c = stats.binom.pmf(c_t, row_sums[1], p_common)
        table_probs.append(prob_a * prob_c)
    
    # Get Fisher's p-value for each possible table
    fisher_p_values = []
    for possible_table in possible_tables:
        _, p_value = stats.fisher_exact(possible_table, alternative=alternative)
        fisher_p_values.append(p_value)
    
    # Calculate Boschloo's p-value as the sum of probabilities of tables
    # with Fisher's p-value <= the observed Fisher's p-value
    boschloo_p = sum(prob for prob, p_val in zip(table_probs, fisher_p_values) 
                     if p_val <= observed_fisher_p)
    
    return statistic, boschloo_p
#*********************
# Joshua H will present on the topic of Cochran’s Q test, creating function named 'cochran_q' 

#*********************
# Paycen H will present on the topic of Phi coefficient test, creating function named 'phicoeff' 

#*********************
# Kyle H will present on the topic of Fisher’s exact test, creating function named 'fisher_exact' 

#*********************
# Emma H will present on the topic of Spearman correlation test, creating function named 'spearmanr' 

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

#*********************
# Alvina Y will present on the topic of F-test for overall regression, creating function named 'f_test' 

#*********************
# Polina Z will present on the topic of Harvey-Collier test, creating function named 'harvey_collier'

#*********************


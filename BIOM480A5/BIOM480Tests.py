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
def mantel_test(matrix_a, matrix_b, permutations=999, random_state=None):
    '''
    Performs a Mantel test to measure correlation between two distance matrices.
    
    Parameters:
    -----------
    matrix_a : array-like
        First distance matrix (square, symmetric)
    matrix_b : array-like
        Second distance matrix (square, symmetric)
    permutations : int, optional (default=999)
        Number of permutations for the test
    random_state : int or None, optional (default=None)
        Random seed for reproducibility
    
    Returns:
    --------
    r : float
        Mantel correlation statistic
    p_value : float
        p-value from the permutation test
        
    Example:
    >>> import numpy as np
    >>> from scipy.spatial.distance import pdist, squareform
    >>> # Create two correlated distance matrices
    >>> coords = np.random.rand(10, 2)
    >>> matrix_a = squareform(pdist(coords, 'euclidean'))
    >>> matrix_b = matrix_a * 0.9 + np.random.rand(10, 10) * 0.1
    >>> matrix_b = (matrix_b + matrix_b.T) / 2  # Make symmetric
    >>> np.fill_diagonal(matrix_b, 0)  # Zero diagonal
    >>> r, p = mantel_test(matrix_a, matrix_b, permutations=99, random_state=42)
    >>> print(f"Mantel statistic r: {r:.4f}, p-value: {p:.4f}")
    Mantel statistic r: 0.9723, p-value: 0.0100
    
    Notes:
    This test evaluates the correlation between two distance matrices using permutation
    to assess statistical significance. It's commonly used in ecology to test for relationships
    between different types of distances (e.g., geographic vs. community composition).
    The matrices must be square, symmetric, and of the same dimensions.
    '''
    # Convert inputs to numpy arrays
    matrix_a = np.asarray(matrix_a)
    matrix_b = np.asarray(matrix_b)
    
    # Check that matrices are square and of the same size
    if matrix_a.shape != matrix_b.shape:
        raise ValueError("Distance matrices must be of the same shape")
    
    # Set random seed if provided
    if random_state is not None:
        np.random.seed(random_state)
    
    # Flatten the distance matrices, ignoring the diagonal and keeping only the lower triangle
    # This avoids double-counting distances and including self-distances
    n = matrix_a.shape[0]
    indices = np.triu_indices(n, k=1)
    a_flat = matrix_a[indices]
    b_flat = matrix_b[indices]
    
    # Calculate the Mantel statistic (correlation coefficient)
    r_obs = np.corrcoef(a_flat, b_flat)[0, 1]
    
    # Permutation test
    r_perm = np.zeros(permutations)
    for i in range(permutations):
        # Shuffle one of the matrices
        indices_perm = np.random.permutation(n)
        b_perm = matrix_b[indices_perm, :][:, indices_perm]
        b_flat_perm = b_perm[indices]
        
        # Calculate correlation for permuted matrix
        r_perm[i] = np.corrcoef(a_flat, b_flat_perm)[0, 1]
    
    # Calculate p-value as proportion of permutations with a correlation
    # greater than or equal to the observed correlation
    p_value = np.sum(np.abs(r_perm) >= np.abs(r_obs)) / permutations
    
    return r_obs, p_value
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


def solve_equations(coeff, values):
    """
    Solving linear equations

    Parameters
    ----------
    coeff : coefficients of the variables in the equation
    values : value of the equations

    Returns
    ----------
    1 numpy matrix
    """

    import numpy as np

    inversed = np.linalg.inv(coeff)
    soln = np.dot(inversed, values)

    return soln

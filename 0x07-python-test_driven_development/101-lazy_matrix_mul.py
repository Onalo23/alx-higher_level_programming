#!/usr/bin/python3
"""defined matrix multiplication function using NumPy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return multiplication of two matrices

    Arguments:
        m_a (list of lists of ints/floats): first matrix
        m_b (list of lists of ints/floats): second matrix
    """

    return (np.matmul(m_a, m_b))

#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
        Calculates the factorial of a given non-negative integer using recursion.

    Parameters:
        n (int): A non-negative integer for which the factorial will be computed.

    Returns:
        int: The factorial value of the input number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Convert command-line argument to int and compute factorial
f = factorial(int(sys.argv[1]))
print(f)

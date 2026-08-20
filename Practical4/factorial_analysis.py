# Implementation and Time Analysis of Factorial
# using Iterative and Recursive Methods

import time


# -------------------------------------------------
# 1. Iterative Method
# -------------------------------------------------
def factorial_iterative(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result


# -------------------------------------------------
# 2. Recursive Method
# -------------------------------------------------
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial_recursive(n - 1)


# -------------------------------------------------
# Main Program
# -------------------------------------------------

print("======================================")
print(" FACTORIAL - ITERATIVE & RECURSIVE")
print("======================================")

n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")

else:
    # -------------------------------
    # Iterative Method
    # -------------------------------
    start_time = time.perf_counter()

    result_iterative = factorial_iterative(n)

    end_time = time.perf_counter()

    iterative_time = end_time - start_time

    # -------------------------------
    # Recursive Method
    # -------------------------------
    start_time = time.perf_counter()

    result_recursive = factorial_recursive(n)

    end_time = time.perf_counter()

    recursive_time = end_time - start_time

    # -------------------------------
    # Display Results
    # -------------------------------

    print("\nFactorial using Iterative Method:")
    print(result_iterative)

    print("\nFactorial using Recursive Method:")
    print(result_recursive)

    print("\n--------------------------------------")
    print("TIME ANALYSIS")
    print("--------------------------------------")

    print("Iterative Time :", iterative_time, "seconds")
    print("Recursive Time :", recursive_time, "seconds")

    print("\n--------------------------------------")
    print("COMPLEXITY ANALYSIS")
    print("--------------------------------------")

    print("Iterative Time Complexity : O(n)")
    print("Iterative Space Complexity: O(1)")

    print("Recursive Time Complexity : O(n)")
    print("Recursive Space Complexity: O(n)")
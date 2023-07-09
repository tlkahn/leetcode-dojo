import timeit
from functools import reduce


def plus_str(a, b):
    return a + b


def compare_string_concatenation():
    # Create two lists of strings
    strings = ["Hello"] * 1000
    more_strings = ["World"] * 1000

    # Using str.join
    join_time = timeit.timeit(lambda: "".join(strings), number=10000)

    # Using the + operator
    plus_time = timeit.timeit(lambda: reduce(plus_str, strings), number=10000)

    # Print the results
    print(f"Using str.join: {join_time} seconds")
    print(f"Using + operator: {plus_time} seconds")


# Run the function
compare_string_concatenation()

# Results:
# Using str.join: 0.07919529199716635 seconds
# Using + operator: 1.0881493340129964 seconds

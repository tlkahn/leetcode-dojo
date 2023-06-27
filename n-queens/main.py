def solve_n_queens(n):
    """
    The function `solve_n_queens(n)` takes an integer `n` as input and returns a list of all
    possible solutions to the N-Queen problem for a board of size `n`. Each solution is
    represented as a list of integers, where each integer represents the column position of
    a queen in a row.

    The `backtrack` function implements the backtracking algorithm to find all possible
    solutions. It takes three lists as input: `queens` stores the column positions of queens
    in the current partial solution, `xy_diff` stores the differences of row and column
    indices for queens in the current partial solution, and `xy_sum` stores the sums of row
    and column indices for queens in the current partial solution.

    The `backtrack` function checks if a queen can be placed in a particular row and column
    by checking if the column is not already occupied by a queen, and if the differences and
    sums of row and column indices are not already occupied by queens. If a queen can be
    placed, the function adds it to the `queens`, `xy_diff`, and `xy_sum` lists and
    recursively calls itself with the updated lists. If a solution is found (i.e., all rows
    are occupied by queens), it is added to the `res` list.

    Finally, the `solve_n_queens` function converts the solutions from integer lists to
    board representations, where "." represents an empty square and "Q" represents a queen.

    """

    def backtrack(queens, xy_diff, xy_sum):
        p = len(queens)
        if p == n:
            res.append(queens)
            return
        for q in range(n):
            if q not in queens and p - q not in xy_diff and p + q not in xy_sum:
                backtrack(queens + [q], xy_diff + [p - q], xy_sum + [p + q])

    res = []
    backtrack([], [], [])
    return [[("." * i) + "Q" + ("." * (n - i - 1)) for i in sol] for sol in res]


def test_solve_n_queens():
    # Test case 1
    n = 4
    expected = [
        [".Q..", "...Q", "Q...", "..Q."],
        ["..Q.", "Q...", "...Q", ".Q.."],
    ]
    assert solve_n_queens(n) == expected

    # Test case 2
    n = 1
    expected = [["Q"]]
    assert solve_n_queens(n) == expected

    # Test case 3
    n = 2
    expected = []
    assert solve_n_queens(n) == expected

    # Test case 4
    n = 8
    expected_len = 92
    ans = solve_n_queens(n)
    assert len(ans) == expected_len

    print("All test cases pass")


test_solve_n_queens()

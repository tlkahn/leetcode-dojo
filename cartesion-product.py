def cartesian_product(*iterables):
    result = [[]]
    for iterable in iterables:
        result = [tuple(x) + (y,) for x in result for y in iterable]
    return result


def test_cartesian_product():
    # Test case 1
    result = cartesian_product([1, 2], [3, 4])
    assert result == [(1, 3), (1, 4), (2, 3), (2, 4)]

    # Test case 2
    result = cartesian_product([1, 2], [3, 4], [5, 6])
    assert result == [
        (1, 3, 5),
        (1, 3, 6),
        (1, 4, 5),
        (1, 4, 6),
        (2, 3, 5),
        (2, 3, 6),
        (2, 4, 5),
        (2, 4, 6),
    ]

    # Test case 3
    result = cartesian_product([1], [2], [3])
    assert result == [(1, 2, 3)]

    # Test case 4
    result = cartesian_product([], [1, 2], [3, 4])
    assert result == []

    print("All test cases pass")


# Run the test cases
test_cartesian_product()

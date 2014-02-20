def get_single_integer(integers):
    """
    Given a list of `integers`, every element appears twice except for one.
    Return that single one.
    """
    if not integers:
        return None
    p = integers[0]
    for i in range(1, len(integers)):
        p = p ^ integers[i]
    return p


def reverse_integer(number):
    t = 0
    if number > 0:
        positive = True
    else:
        positive = False
        number = -number
    while number != 0:
        t = 10 * t + number % 10
        number /= 10
    return t if positive else -t


def max_subarray(a):
    """
    Maximum subarray problem

    In case of all negative numbers, zero-length subarrays does not count.
    http://en.wikipedia.org/wiki/Maximum_subarray_problem
    """
    if not a:
        raise Exception('The input array must contain at least one number.')
    max_sum = a[0]

    # Initialize a list `m` of same size of a (which may be redundant for this
    # problem alone.
    # `m[i]` represents the max sum of all subarrays ending `i`
    m = [0] * len(a)
    m[0] = max_sum
    for i in range(1, len(a)):
        m[i] = max(a[i], m[i - 1] + a[i])

    # Find the largest in `m`
    for e in m:
        if e > max_sum:
            max_sum = e
    return max_sum


if __name__ == '__main__':
    assert reverse_integer(-173) == -371
    assert reverse_integer(976) == 679
    assert reverse_integer(500) == 5
    assert reverse_integer(0) == 0
    a = [2, 5, 5, 8, 9, 6, 2, 3, 9, 3, 6]
    assert get_single_integer(a) == 8
    b = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    c = [-3, -4, -5, -1, -9]
    assert max_subarray(b) == 6
    assert max_subarray(c) == -1

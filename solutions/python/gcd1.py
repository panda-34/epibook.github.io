# @include
def GCD(x, y):
    if x == 0:
        return y
    elif y == 0:
        return x
    elif not x & 1 and not y & 1:  # x and y are even.
        return GCD(x >> 1, y >> 1) << 1
    elif not x & 1 and y & 1:  # x is even, y is odd.
        return GCD(x >> 1, y)
    elif x & 1 and not y & 1:  # x is odd, y is even.
        return GCD(x, y >> 1)
    elif x > y:  # Both x and y are odd, x > y.
        return GCD(x - y, y)
    return GCD(x, y - x)  # Both x and y are odd, x <= y.
# @exclude

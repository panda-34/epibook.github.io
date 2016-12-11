# @include
def GCD(x, y):
    return x if y == 0 else GCD(y, x % y)
# @exclude

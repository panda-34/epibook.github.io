def comp(x):
    return (x[1], x[0])


A = [[1, 1], [3, 1], [2, 1], [4, 4]]
A.sort(key=comp)
print(A)

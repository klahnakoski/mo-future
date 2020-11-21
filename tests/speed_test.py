from timeit import timeit

a = [1, 2, 3]
b = [4, 5, 6]

t = timeit("tuple(a)+tuple(b)\npass", number=1 * 1000 * 1000, globals=globals())
print(t)

t = timeit("c=tuple(a+b)\npass", number=1 * 1000 * 1000, globals=globals())
print(t)

t = timeit("a.append(b)\nc=tuple(a)", number=100 * 1000, globals=globals())
print(t)

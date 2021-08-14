# exercises

lst = [99, "no data", 95, 94, "no data"]


def foo(lst):
    return [i if not isinstance(i, str) else 0 for i in lst]


print(foo(lst))

# fn that converts strings to floats, then sums items
flst = ["1.2", "2.6", "3.3"]


def foo(flst):
    return sum(float(i) for i in flst)


print(foo(flst))

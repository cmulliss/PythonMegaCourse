def area(a, b):
    return a * b


print(area(4, 5))


# 2 strings as parameters and cats them
def stringcat(st1, st2):
    return st1 + st2


print(stringcat("this ", "that"))

# a default value for a parameter
def circumf(a, b=2.174):
    return a * b


print(circumf(a=4))
# or
print(circumf(4))

# fn with many args
def mean(*args):
    return args


# # gives a tuple
print(mean(1, 2, "a", 4))

# # what can we do with the tuple?
def mean(*args):
    return sum(args) / len(args)


print(mean(1, 2, 3, 4, 5, 6))

# average fn
print("Average fn")


def average(*args):
    return sum(args) / len(args)


print(average(8, 9, 10))

# indefinite number of strings, sorted alphabetically and UC.
str_list = ["snow", "glacier", "iceberg"]


def strings(*args):
    args = [x.upper() for x in args]
    return sorted(args)


print(strings("snow", "glacier", "iceberg"))

# keyword args use ** kwargs need names, not just numbers, you get a dictionary: {'a': 1, 'b': 2, 'c': 3} items where each key is name of args.
print("keyword args")


def mean(**kwargs):
    return kwargs


print(mean(a=1, b=2, c=3))

# exercise


def find_sum(**kwargs):
    return sum(kwargs.values())


print(find_sum(a=3, b=2, c=4))

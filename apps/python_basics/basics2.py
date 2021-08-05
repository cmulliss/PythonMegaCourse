# creating functions
# mean


def mean(myList):
    the_mean = sum(myList) / len(myList)
    return the_mean


print(mean([7, 8, 9]))

print(type(mean), type(sum))


def calculate_length(lst):
    the_length = len(lst)
    return the_length


print(calculate_length([1, 2, 3]))


def squareIt(myNumber):
    return myNumber * myNumber


print(squareIt(3))


def convert_vol(ounces):
    return ounces * 29.57353


print(convert_vol(2))

# conditionals

a, b = 10, 20
min = a if a < b else b

print(min)



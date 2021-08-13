# temps = [221, 234, 340, 230]

# new_temps = []
# for temp in temps:
#     new_temps.append(temp / 10)

# print(new_temps)

# where to store each temp? In a new list
# above is ok, but neater way to do this, using 'list comprehension', a way of creating lists without using 'for' loop.

# you don't have to create an empty list, because a list will be generated dynamically.


temps = [221, 234, 340, 230]

new_temps = [temp / 10 for temp in temps]
print(new_temps)

# we want to ignore the -9999, just adding a conditional to check if different to -9999
temps2 = [221, 234, 340, -9999, 230]
new_temps2 = [temp2 / 10 for temp2 in temps2 if temp2 != -9999]
print(new_temps2)

lst = [99, "no data", 95, 94, "no data"]


def foo(lst):
    return [i for i in lst if isinstance(i, int)]


print(foo(lst))

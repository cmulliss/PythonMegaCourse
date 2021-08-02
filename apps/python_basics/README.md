# Python

Python got its name not from the snake, but from Monty Python's Flying Circus, a favorite comedy series of Guido van Rossum, the creator of Python

## Ranges

You can create a list of numbers automatically using a range. For example:

list(range(1, 10))

That will output:

[1, 2, 3, 4, 5, 6, 7, 8, 9]

As you can see we just needed to specify the list boundaries inside range(). So, we specified 1and 10. Note that 10 is not included in the list. The generated list always runs up to one number before the upper number. In our example, it goes up to 9 since the upper number is 10.

You can also specify a step as a third argument:

list(range(1, 10, 2))

That will output:

[1, 3, 5, 7, 9]

So, the count happens every two items starting from 1 and ending at 9.

## dictionary

uses {} and contains items, with key: value pairs
student_grades = {'Harry': 9.1, 'Sim': 9.8, 'John': 7.5}

# tuple

list using ()
they are **immutable**

## Built in shell

in terminal: python3, then

dir(list) or whatever

help(str.upper)

q to quit and return to shell

'hello'.upper()
'HELLO'

clear l to clear shell

**dir shows methods**, but can also use **functions, like print**, using:

dir(\_\_builtins\_\_)

gives complete list of functions

pop to remove item from a position

l = list(range(10))
print(l)

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(l.pop(0))

0

print(l)

[1, 2, 3, 4, 5, 6, 7, 8, 9]

print(l.pop(3))

4

print(l)

[1, 2, 3, 5, 6, 7, 8, 9]

You can use negative values to specify the position from the end. The index at the end is -1.

print(l.pop(-2))
8

print(l)
[1, 2, 3, 5, 6, 7, 9]

## Cheatsheet (Data Types)

In this section, you learned that:

Integers are for representing whole numbers:

rank = 10
eggs = 12
people = 3
Floats represent continuous values:

temperature = 10.2
rainfall = 5.98
elevation = 1031.88
Strings represent any text:

message = "Welcome to our online shop!"
name = "John"
serial = "R001991981SW"
Lists represent arrays of values that may change during the course of the program:

members = ["Sim Soony", "Marry Roundknee", "Jack Corridor"]
pixel_values = [252, 251, 251, 253, 250, 248, 247]
Dictionaries represent pairs of keys and values:

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
volcano_elevations = {"Glacier Peak": 3213.9, "Rainer": 4392.1}
Keys of a dictionary can be extracted with:

phone_numbers.keys()
Values of a dictionary can be extracted with:

phone_numbers.values()
Tuples represent arrays of values that are not to be changed during the course of the program:

vowels = ('a', 'e', 'i', 'o', 'u')
one_digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
To find out what attributes a type has:

dir(str)
dir(list)
dir(dict)
To find out what Python builtin functions there are:

dir(**builtins**)
Documentation for a Python command can be found with:

help(str)
help(str.replace)
help(dict.values)

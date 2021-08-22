# Python

Python got its name not from the snake, but from Monty Python's Flying Circus, a favorite comedy series of Guido van Rossum, the creator of Python

install homebrew then
brew install python3

## Lists

in shell, use:

dir(list) and will mostly use the ones at end without double underscores

'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

monday_temperatures = [9.1, 8.8, 7.5]

want to use append so in shell, help(list.append)

monday_temperatures.append(8.1)
print(monday_temperatures)

in shell

help(list.index)

Help on method_descriptor:

index(self, value, start=0, stop=9223372036854775807, /)
Return first index of value.

    Raises ValueError if the value is not present.

can also use negative indexing, so 

### negative indexing

print(monday_temperatures[-2])

will give 2nd from end

### Ranges

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

getting an item with via its index

- monday_temperatures.\_\_getitem\_\_(1)
  gives item with index 1

but don't need this double underscore method, can just do:
monday_temperatures[1]

can access one item
monday_temperatures[3] for fourth temp

but can also access portions of a list
monday_temperatures[0:3]
will give first 3, to get first 4 would need to do 0:5 or :5

to get to last item on list use 2:

### dictionary

uses {} and contains items, with key: value pairs
student_grades = {'Harry': 9.1, 'Sim': 9.8, 'John': 7.5}

student_grades = {"Harry": 9.1, "Sim": 9.8, "John": 7.5}
student_grades["Sim"]
print(student_grades["Sim"])
returns
9.8

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

## Tip: Converting Between Datatypes

Sometimes you might need to convert between different data types in Python for one reason or another. That is very easy to do:

From tuple to list:

>>> data = (1, 2, 3)
>>> list(data)
[1, 2, 3]
From list to tuple:

>>> data = [1, 2, 3]
>>> tuple(data)
(1, 2, 3)
From list to dictionary:

>>> data = [["name", "John"], ["surname", "smith"]]
>>> dict(data)
{'name': 'John', 'surname': 'smith'}
Note that the original data type needs to have the data structured in a way that can be understood by the new data type. For example, the following would not work:

>>> data = [1, 2, 3]
>>> dict(data)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
That's because a dictionary is made of key and value pairs, but the list was not constructed that way, so the above would generate an error.

## Cheatsheet (Operations with Data Types)

In this section, you learned that:

Lists, strings, and tuples have a positive index system:

["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
   0      1      2      3      4      5      6
And a negative index system:

["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  -7     -6     -5     -4     -3     -2     -1
In a list, the 2nd, 3rd, and 4th items can be accessed with:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[1:4]
Output: ['Tue', 'Wed', 'Thu']
First three items of a list:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:3]
Output:['Mon', 'Tue', 'Wed'] 
Last three items of a list:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[-3:]
Output: ['Fri', 'Sat', 'Sun']
Everything but the last:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:-1] 
Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 
Everything but the last two:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:-2] 
Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'] 
A single in a dictionary can be accessed using its key:

phone_numbers = {"John Smith":"+37682929928","Marry Simpsons":"+423998200919"}
phone_numbers["Marry Simpsons"]
Output: '+423998200919'
Fullscreen

### Ternary Operator in Python

Copy value of a in min if a < b else copy b

a, b = 10, 20
min = a if a < b else b
  
print(min)

## Built in modules

 all are written in C language, like python

in shell:
>>> import sys
>>> sys.builtin_module_names
will list them all

dir(time) for example will show how to use it

then

>>> help(time.sleep)

shows how to use it, eg:

>>> time.sleep(3)

gives 3 second delay

### Standard python modules

>>> import sys
>>> import os
>>> sys.prefix
'/Library/Frameworks/Python.framework/Versions/3.9'

then in terminal:

open /Library/Frameworks/Python.framework/Versions/3.9
cherry@Cs-MacBook-Pro 3.9

will bring up window, within which, choose lib, python3.9, will see all standard python modules, all are python code.
use dir to see what available for each, eg:

dir(path)

### loading json

use json standard library
import json

data = json.load


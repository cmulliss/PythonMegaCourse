# Python got his name not from the snake, but from Monty Python's Flying Circus, a favorite comedy series of Guido van Rossum, the creator of Python

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

## Built in shell

in terminal: python3, then

dir(list) or whatever

help(str.upper)

q to quit and return to shell

'hello'.upper()
'HELLO'

**dir shows methods**, but can also use **functions, like print**, using:

dir(\_\_builtins\_\_)

gives complete list of functions

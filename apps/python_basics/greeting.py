user_input = input("Enter your name:")
print("Welcome", user_input)

# or can use:
user_input = input("Enter your name: ")
message = "Greetings %s! " % user_input
print(message)
# the variable, user_input, will replace %s
# %s special string in python
# ! is a normal string,
# then the final % before the variable, the variable will replace %s

your_input = input("Enter your name ")
# # for python 2, and 3 with multiple input
greeting = "Welcome %s! " % your_input
# or can do, need to add prefix f, just outside the quotes:
greeting = f"Welcome {user_input}"
print(greeting)

name = input("Enter your name ")
surname = input("Enter your surname ")

message = "Hello %s %s" % (name, surname)
# message = f"Hello {user_input}" doesn't work
message = f"Welcome {name} {surname}"
print(message)


def hi(name):
    return "Hi %s" % name


# # case
def foo(name):
    print("Hi %s" % name.title())


# redo this for 2 names!


def greeting():
    first_name = input("Enter your First Name: ")
    first_name_to_up = first_name.upper()
    return "Hello %s" % first_name_to_up


print(greeting())

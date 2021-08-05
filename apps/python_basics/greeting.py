# user_input = input("Enter your name:")
# print("Welcome", user_input)

# or can use:
user_input = input("Enter your name: ")
message = "Greetings %s! " % user_input
print(message)
# the variable, user_input, will replace %s
# %s special string in python
# ! is a normal string,
# then the final % before the variable, the variable will replace %s

your_input = input("Enter your name ")
greeting = "Welcome %s! " % your_input
print(greeting)

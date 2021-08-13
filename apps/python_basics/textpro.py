# Say something: its good weather today
# Say something: How is the weather there
# Say something: there are some clouds here
# Say something: \end


def sentence_maker(phrase):
    interrogatives = ("how", "what", "why", "who")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)


results = []
while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))
print(" ".join(results))


# want to store the phrases the user enters in a list, start with 'results' with an empty list outside the loop. So python will execute the fn definition, create the empty list and then start the loop.
# can use string 'join' method.

# how can we get the actual strings? We are appending to the list the strings the user entered. we have a fn that can conver those strings into sentences, to call the fn need user_input.

# define a fn at top, then create a loop, ask user for input on each iteration, immediately check

# finally concatenate the output using 'join' and print the results.

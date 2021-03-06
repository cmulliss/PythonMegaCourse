import json
from difflib import get_close_matches
from os import readlink
from typing import ItemsView

data = json.load(open("/Users/cherry/repos/PythonMegaCourse/apps/dictionary/data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input(
            "Did you mean %s instead? Enter Y if yes, or N if no: "
            % get_close_matches(w, data.keys())[0]
        )
        if yn.upper() == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn.upper() == "N":
            return "This word is not in the dictionary, please check."
        else:
            return "we didn't understand your entry, please try again. "

    else:
        return "This word is not in the dictionary, please check"


word = input("Enter word: ")

output = translate(word)

if type(output) == list:

    for item in output:
        print(item)
    else:
        print(output)


# /Users/cherry/repos/PythonMegaCourse/apps/dictionary/data.json

# sequence matching with difflib and SequenceMatcher

# elif for more than 2 conditionals
# apps/dictionary/data.json

# finally, want to format output to show multiple definitions as separate lines.

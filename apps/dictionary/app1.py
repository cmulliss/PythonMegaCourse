import json

data = json.load(open("data.json"))


def translate(dictword):
    return data[dictword]


word = input("Enter word: ")

print(translate(word))

# /Users/cherry/repos/PythonMegaCourse/apps/dictionary/data.json

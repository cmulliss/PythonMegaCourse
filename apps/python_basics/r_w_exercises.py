with open(
    "/Users/cherry/repos/PythonMegaCourse/apps/python_basics/text_files/bear.txt", "r"
) as myfile:
    content = myfile.read()
print(content[:90])

# define a fn that gets a single string character and a filepath as parameters ands returns the number of occurances of that character in the file.


def foo(
    character,
    filepath="/Users/cherry/repos/PythonMegaCourse/apps/python_basics/text_files/bear.txt",
):
    file = open(filepath)
    content = file.read()
    return content.count(character)


print(
    foo(
        "c",
        "/Users/cherry/repos/PythonMegaCourse/apps/python_basics/text_files/bear.txt",
    )
)

# create a file file.txt and write the text 'snail' there.
with open(
    "/Users/cherry/repos/PythonMegaCourse/apps/python_basics/text_files/file.txt", "w"
) as myfile:
    myfile.write("snail")
print(myfile)

# create first.txt file wht contains the 1st 90 chars of bear.txt.

with open(
    "/Users/cherry/repos/PythonMegaCourse/apps/python_basics/text_files/bear.txt", "r"
) as myfile:
    content = myfile.read()


with open(
    "/Users/cherry/repos/PythonMegaCourse/apps/python_basics/text_files/first.txt", "w"
) as myfile2:
    new_content = myfile2.write(content[:90])

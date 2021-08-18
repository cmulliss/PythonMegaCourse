with open(
    "/Users/cherry/repos/PythonMegaCourse/apps/python_basics/text_files/fruit.txt", "a+"
) as myfile:
    myfile.write("\nclementine")
    myfile.seek(0)
    content = myfile.read()
print(content)

# need to add a + to make readable, and use seek to put cursor at zero position.

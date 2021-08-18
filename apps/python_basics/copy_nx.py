with open(
    "/Users/cherry/repos/PythonMegaCourse/apps/python_basics/text_files/data.txt", "r"
) as myfile:
    content = myfile.read()
with open(
    "/Users/cherry/repos/PythonMegaCourse/apps/python_basics/text_files/data.txt", "a+"
) as myfile:
    myfile.write(content)
    myfile.write(content)

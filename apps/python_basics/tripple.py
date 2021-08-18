# use python to repeat content of data.txt so appears 3 times.

with open(
    "/Users/cherry/repos/PythonMegaCourse/apps/python_basics/text_files/data.txt", "a+"
) as file:
    file.seek(0)
    content = file.read()
    file.seek(0)
    file.write(content)
    file.write(content)

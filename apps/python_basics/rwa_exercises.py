with open(
    "/Users/cherry/repos/PythonMegaCourse/apps/python_basics/text_files/bear1.txt", "r"
) as file:
    content = file.read()

with open(
    "/Users/cherry/repos/PythonMegaCourse/apps/python_basics/text_files/bear2.txt", "a+"
) as file2:
    file2.write(content)

    # next exercise

    with open(
        "/Users/cherry/repos/PythonMegaCourse/apps/python_basics/text_files/bear1.txt",
        "r",
    ) as file:
        content = file.read()

    with open(
        "/Users/cherry/repos/PythonMegaCourse/apps/python_basics/text_files/bear2.txt",
        "a",
    ) as file:
        file.write(content)

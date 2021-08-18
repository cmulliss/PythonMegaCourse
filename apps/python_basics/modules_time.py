import time

while True:

    with open(
        "/Users/cherry/repos/PythonMegaCourse/apps/python_basics/text_files/vegetables.txt"
    ) as file:
        print(file.read())
        time.sleep(10)

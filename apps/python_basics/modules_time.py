import os
import time

while True:
    if os.path.exists(
        "/Users/cherry/repos/PythonMegaCourse/apps/python_basics/text_files/vegetables.txt"
    ):
        with open(
            "/Users/cherry/repos/PythonMegaCourse/apps/python_basics/text_files/vegetables.txt"
        ) as file:
            print(file.read())
    else:
        print("File does not exist")
    time.sleep(10)

# want to check file exists

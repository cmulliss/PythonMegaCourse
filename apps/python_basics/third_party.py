import os
import time

import pandas

while True:
    if os.path.exists(
        "/Users/cherry/repos/PythonMegaCourse/apps/python_basics/files/temps_today.csv"
    ):
        data = pandas.read_csv(
            "/Users/cherry/repos/PythonMegaCourse/apps/python_basics/files/temps_today.csv"
        )
        print(data.mean()["st1"])

    else:
        print("File does not exist")
    time.sleep(10)

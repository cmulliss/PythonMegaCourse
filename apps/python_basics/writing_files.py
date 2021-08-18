# for reading use r, for writing use w
# veg file does not exist, will be created by the 'open' fn

with open(
    "/Users/cherry/repos/PythonMegaCourse/apps/python_basics/text_files/veg.txt", "w"
) as myfile:
    myfile.write("Tomato\nCucumber\nRadish\nSwede")
    myfile.write("\nGarlic")

# if file exists will overwrite the existing file, so for multiple items need \n


# reading text from a file, use open, give path

# myfile = open(
#     "/Users/cherry/repos/PythonMegaCourse/apps/python_basics/text_files/fruits.txt"
# )
# better way of doing this, use 'with open'
with open(
    "/Users/cherry/repos/PythonMegaCourse/apps/python_basics/text_files/fruits.txt"
) as myfile:
    content = myfile.read()
print(content)
print(content)

# print(myfile.read())
# print(myfile.read())


# myfile.close()
# using with open no need to close file, closes file implicitly.


# cursor is left at bottom of file following first read, so will bet blank space, notrepeated list. Can save the content in a variable, then print it as many times as you wish.

# when you create a file object, a file object is created in RAM and is going to remain there until the execution of prog ends. Best to close prog, then just dealing with the variable you have created.

# /Users/cherry/repos/PythonMegaCourse/apps/python_basics/text_files/fruits.txt

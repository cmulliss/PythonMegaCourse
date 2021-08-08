# def greeting():
#     first_name = input("Enter your First Name: ")
#     first_name_to_up = first_name.upper()
#     return "Hello %s" % first_name_to_up


# print(greeting())

# dictionaries again
student_grades = {"Harry": 9.1, "Sim": 9.8, "John": 7.5}
student_grades["Sim"]
print(student_grades["Sim"])

print("*******")

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for value in phone_numbers.values():
    new_dict = value.replace("+", "00")
    print(new_dict)

print("*******")



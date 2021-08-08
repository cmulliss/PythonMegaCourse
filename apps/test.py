def greeting():
    first_name = input("Enter your First Name: ")
    first_name_to_up = first_name.upper()
    return "Hello %s" % first_name_to_up


print(greeting())

print("*******")

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for value in phone_numbers.values():
    return value.replace("+", "00")


print("*******")

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

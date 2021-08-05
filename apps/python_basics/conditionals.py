def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean


monday_temperatures = [4, 5, 6]

student_grades = {"Harry": 7, "Sim": 8, "John": 9}

print("student grades")
print(mean(student_grades))


print("monday temps")
print(mean(monday_temperatures))


def foo(x, array):
    if x in array:
        return True
    else:
        return False


print(foo(1, [1, 2, 3]))
print(foo(1, [2, 3]))
print(foo(1, ["1", 2, 3]))


def pwdlength(password):
    if len(password) < 8:
        return False
    else:
        return True


print("password")
print(pwdlength("lasdk"))


def temp(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"


print(temp(10))
print(temp(6))

def temp(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"


print(temp(10))
print(temp(6))


def temp(temperature):
    if temperature > 25:
        return "Hot"
    elif 25 >= temperature >= 15:
        return "Warm"
    else:
        return "Cold"


print(temp(10))
print(temp(16))
print(temp(30))

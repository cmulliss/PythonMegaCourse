def weather_condition(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"


# fails without adding a float type so not comparing a str with an int
user_input = float(input("Enter temperature:"))

print("You entered:", user_input)
print("Which is ", weather_condition(user_input))

# if enter a number in input, will show type str
user_input = input("Enter some input:")
print(type(user_input))

# float is better option than int
user_input = float(input("Enter temperature:"))

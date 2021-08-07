monday_temperatures = [9.1, 8.8, 7.6]

# first temp
print(monday_temperatures[0])
# rounded
print(round(monday_temperatures[0]))

# rounded for multiple list items, loops through in turn
monday_temperatures = [9.1, 8.8, 7.6]

for temperature in monday_temperatures:
    print(round(temperature))
    print("Done")

for letter in "hello":
    # print the letters
    # print(letter)
    # initial caps
    print(letter.title())

print("*******")

colors = [11, 34, 98, 43, 45, 54, 54]

for color in colors:
    print(color)

print("*******")

colors = [11, 34, 98, 43, 45, 54, 54]
for color in colors:
    if color > 50:
        print(color)

print("*******")

colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for color in colors:
    if isinstance(color, int):
        print(color)

print("*******")

colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for color in colors:
    if isinstance(color, int) and color > 50:
        print(color)

print("*******")
# looping through a dictionary
student_grades = {"Harry": 9.1, "Sim": 9.8, "John": 7.5}

print("*******")

for grades in student_grades.items():
    print(grades)

for grades in student_grades.keys():
    print(grades)

for grades in student_grades.values():
    print(grades)

day_hours = 24
week_days = 7

week_hours = day_hours * week_days

year_days = 365

year_hours = day_hours * year_days

print("hours in a week:", week_hours)
print("hours in a year:", year_hours)

x = 10
y = "10"
z = 10.7

print(x * x, y + y)

print(type(x), type(y), type(z))

student_grades = [9.1, 8.8, 7.5]

mySum = sum(student_grades)

length = len(student_grades)

mean = mySum / length
print(mean)

max_value = max(student_grades)
print(max_value)

student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
print(student_grades.count(10.0))

student_grades = [9.1, 8.8, 7.5]
student_grades = {"Harry": 9.1, "Sim": 9.8, "John": 7.5}
print(student_grades.values())
print(student_grades.keys())

monday_temps = (1, 4, 5)
monday_temps2 = [1, 4, 5]
monday_temps2.append(6)
# monday_temps.append(6)
print(monday_temps2)
print(monday_temps)

monday_temps2.remove(4)
print(monday_temps2)

monday_temperatures = [9.1, 8.8, 7.5, 11.1, 10.4]
#  want to use append so in shell, help(list.append)
monday_temperatures.append(8.1)
print(monday_temperatures)
print(monday_temperatures.index(9.1))
print(monday_temperatures)

# this will give the list item index 1
print(monday_temperatures[1])

monday_temperatures = [9.1, 8.8, 7.5, 11.1, 10.4]

# Will give 3 items, 1st, 2nd, 3rd
print(monday_temperatures[:3])

# will give 4th and 5th
print(monday_temperatures[3:])

# negative indexing
print(monday_temperatures[-2])

# and to slice it:
# negative indexing will give last 2 numbers
print(monday_temperatures[-2:])

# last 3 letters
letters = ["a", "b", "c", "d", "e", "f", "g"]
print(letters[-3:])

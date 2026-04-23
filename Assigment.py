# Section 1: Lists (Methods & Slicing)

# 1. The End Goal
market = ["Yam", "Tomato", "Onion"]
market.append("Fish")
print(market)

# 2. Precise Entry
grades = [80, 90, 70]
grades.insert(1, 85)
print(grades)

# 3. The Cleanup
gadgets = ["Laptop", "Phone", "Tablet", "Phone"]
gadgets.remove("Phone")
print(gadgets)

# 4. Wipe Out
colors = ["Red", "Blue", "Green"]
colors.clear()
print(colors)

# 5. Frequency Check
votes = ["Yes", "No", "Yes", "Yes", "No"]
print(votes.count("Yes"))

# 6. The Slice
alphabets = ["a", "b", "c", "d", "e", "f"]
print(alphabets[2:5])

# 7. Flip It
students = ["Kofi", "Ama", "Yaw"]
students.reverse()
print(students)

# 8. Merging
list_a = [1, 2]
list_b = [3, 4]
list_a.extend(list_b)
print(list_a)

# 9. The Pop
cities = ["Accra", "Kumasi", "Tamale"]
removed_city = cities.pop(2)
print(removed_city)
print(cities)

# 10. The Search
items = ["Pen", "Ruler", "Eraser"]
print(items.index("Ruler"))

# Section 2: Tuples & Data Types

# 1. The Tuple Wall
student_info = ("Araba", 20)
# student_info[1] = 21  <-- This would cause: TypeError: 'tuple' object does not support item assignment

# 2. The Switch
tup = (1, 2, 3)
temp_list = list(tup)
temp_list.append(4)
tup = tuple(temp_list)
print(tup)

# 3. Count the Items
data = (10, 20, 10, 30, 10)
print(data.count(10))

# 4. Position Finder
colors = ("Red", "Blue", "Green")
print(colors.index("Blue"))

# 5. Unpacking
coords = (5.6, -0.1)
lat, lon = coords
print(lat)
print(lon)

# 6. Nesting
nest = []
nest.append((5, 10))
print(len(nest))

# 7. Tuple Slicing
numbers = (10, 20, 30, 40, 50)
print(numbers[-2:])

# 8. Mixed Extend
my_list = [1, 2]
my_list.extend((3, 4))
print(my_list)

# 9. Memory Wipe
my_tup = (1, 2, 3)
del my_tup

# 10. Type Check
x = (5)
y = (5,)
print(type(x)) # Returns <class 'int'>
print(type(y)) # Returns <class 'tuple'>

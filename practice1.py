# Strings
name = "Arafat"
print(f"Hello, {name.upper()}!")

# Lists
nums = [1, 2, 3, 4, 5]
print(nums[1:4])   # slicing
print([n * 2 for n in nums])  # list comprehension

print(nums[-2:])
print(nums[2:])

nums = [1, 2, 3, 4, 5]
squares = [n * n for n in nums]
print(squares)  

# Tuples
point = (10, 20)
x, y = point  # unpacking
print(x, y)

# Dicts
person = {"name": "Arafat", "role": "developer"}
for key, value in person.items():
    print(key, "->", value)

# Truthiness
if []:
    print("List is truthy")
else:
    print("Empty list is falsy")

students = [("Ali", 3), ("Zara", 5), ("John", 2)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)  # [('John', 2), ('Ali', 3), ('Zara', 5)]
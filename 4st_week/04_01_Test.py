users = [
    {"name": "Charlie", "age": 35},
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 30},
    {"name": "David", "age": 25}
]

result = sorted(users, key=lambda user: (user["age"], user["name"]))
print(result)




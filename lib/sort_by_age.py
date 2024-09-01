# List of tuples with names and ages
person = [
    ("Brother", 15),
    ("Sister", 33),
    ("Man", 24),
    ("Boy", 88),
    ("Girl", 68),
    ("Queen", 73),
    ("King", 91)
]


def sort_by_age(person_list):
    return sorted(person_list, key=lambda x: x[1])


sorted_person = sort_by_age(person)
print(sorted_person)

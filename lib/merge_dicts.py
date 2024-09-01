# Sorting a List of Tuples by Age
person = [
    ("Brother", 15),
    ("Sister", 33),
    ("Man", 24),
    ("Boy", 88),
    ("Girl", 68),
    ("Queen", 73),
    ("King", 91)
]

def sort_by_age(person_tuple):
    return person_tuple[1]

person.sort(key=sort_by_age)
print("Sorted list by age:", person)


def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()  

    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value  
        else:
            merged_dict[key] = value  

    return merged_dict


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

merged_result = merge_dicts(dict1, dict2)
print("Merged dictionary:", merged_result)

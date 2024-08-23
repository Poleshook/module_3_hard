def calculate_structure_sum(data_structure):
    a = 0
    if isinstance(data_structure, dict):
        for key, value in data_structure.items():
            a += calculate_structure_sum(key)
            a += calculate_structure_sum(value)
    elif isinstance(data_structure, (int, float)):
        a += data_structure
    elif isinstance(data_structure, str):
        a += len(data_structure)
    elif isinstance(data_structure, (list, tuple, set)):
        for i in data_structure:
            a += calculate_structure_sum(i)
    return a

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
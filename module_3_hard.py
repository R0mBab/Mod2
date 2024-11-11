def calculate_structure_sum(*data_structure):
    overall_result = 0
    for i in data_structure:
        if isinstance(i, int):
            overall_result += i
        elif isinstance(i, str):
            overall_result += len(i)
        elif isinstance(i, list):
            overall_result += sum(calculate_structure_sum(item) for item in i)
        elif isinstance(i, tuple):
            overall_result += sum(calculate_structure_sum(item) for item in i)
        elif isinstance(i, dict):
            overall_result += sum(calculate_structure_sum(key) + calculate_structure_sum(value)
                                  for key, value in i.items())
        elif isinstance(i, set):
            overall_result += sum(calculate_structure_sum(item) for item in i)
    return overall_result
result = calculate_structure_sum(
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
)

print(result)

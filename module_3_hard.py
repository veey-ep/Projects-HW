def calculate_structure_sum(my_list):
    res = 0
    if isinstance(my_list, dict):
        my_dict = my_list.items()
        res += sum_index(my_dict)
    elif isinstance(my_list, tuple) or isinstance(my_list, list):
        res += sum_index(my_list)
    elif isinstance(my_list, set):
        my_set = []
        for i in range(len(my_list)):
            my_set.append(my_list.pop())
        res += sum_index(my_set)
    return res
def sum_index(sum_list):
    res = 0
    for i in sum_list:
        if isinstance(i, int) or isinstance(i, float):
            res += i
        elif isinstance(i, str):
            res += len(i)
        else:
            res += calculate_structure_sum(i)
    return res

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
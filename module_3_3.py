def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params(b = 25)
print_params(c = [1,2,3])
values_list = [1, 'two', True]
values_dict = {'a' : False, 'b' : 333, 'c' : 'egge'}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [96, 'chinazes']
print_params(*values_list_2, 42)
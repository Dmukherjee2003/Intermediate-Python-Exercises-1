def get_combined_dict(dict_a, dict_b):
    dict_c = {}
    for i, j in dict_a.items():
        if i in dict_b:
            dict_c[i]= j + dict_b[i]
          
    return dict_c



my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
a = get_combined_dict(my_dict_1,my_dict_2)
print(a)
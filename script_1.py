def get_unique_list(list): 
    arr = []
    for i in list:
        if i not in arr:
            arr.append(i)
    return arr


alist = [1, 2, 3, 2, 1, 4]
result = get_unique_list(alist)
print(result)

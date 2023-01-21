def count_letters(string):
    dict_a = {}
    word = word.lower()
    letters = word.replace(" ", "")
    count = 1
    for i in letters:
            if letters.count(i) > 1:
                count = letters.count(i)
                dict_a[i] = count
            else:
                dict_a[i] = 1
    return dict_a


word = "Hello World"
print(count_letters(word))
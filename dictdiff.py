def dictdiff(dict1, dict2):
    dict_to_return = {}
    for k in dict1.keys():
        if k not in dict2:
            dict_to_return[k] = [dict1[k], None]
        else:
            if dict1[k] != dict2[k]:
                dict_to_return[k] = [dict1[k], dict2[k]]
    for k in dict2.keys():
        if k not in dict1:
            dict_to_return[k] = [None, dict2[k]]

    return dict_to_return


def dictdiff2(dict1, dict2):
    dict_to_return = {}
    all_keys = dict1.keys() | dict2.keys()
    for k in all_keys:
        if dict1.get(k) != dict2.get(k):
            dict_to_return[k] = [dict1.get(k), dict2.get(k)]

    return dict_to_return


d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 1, 'b': 2, 'c': 4}
print(dictdiff(d1, d1))
print(dictdiff(d1, d2))

d3 = {'a': 1, 'b': 2, 'd': 3}
d4 = {'a': 1, 'b': 2, 'c': 4}
print(dictdiff(d3, d4))

d5 = {'a': 1, 'b': 2, 'd': 4}
print(dictdiff(d1, d5))


print(dictdiff2(d1, d1))
print(dictdiff2(d1, d2))
print(dictdiff2(d3, d4))
print(dictdiff2(d1, d5))
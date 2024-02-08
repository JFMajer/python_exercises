def str_sort(str1: str) -> str:
    return ''.join(sorted(str1))


str1 = str_sort("cuba")
print(str1)

def func2(str1: str) -> None:
    splited = str1.split()
    new_str = ', '.join(sorted(splited))
    print(new_str)

func2("Tom Bob Harry")
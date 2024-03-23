def join_numbers(r) -> str:
    return ','.join([str(num) for num in r])


print(join_numbers(range(15)))

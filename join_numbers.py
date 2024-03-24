def join_numbers(r) -> str:
    return ','.join([str(num) for num in r])


def join_numbers_limited(r) -> str:
    return ','.join([str(num) for num in r if 0 < num <= 10])


print(join_numbers(range(15)))
print(join_numbers_limited(range(15)))


def join_numbers_gen(r) -> str:
    return ','.join((str(num) for num in r))


print(join_numbers_gen(range(100)))

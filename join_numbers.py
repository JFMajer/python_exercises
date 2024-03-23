def join_numbers(r) -> str:
    nums = [str(num) for num in r]
    return ','.join(nums)


print(join_numbers(range(15)))

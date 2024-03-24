def sum_numbers(str1: str) -> int:
    only_ints = [int(x) for x in str1.split() if x.isdigit()]
    return sum(only_ints)


print(sum_numbers("10 abc 20 de44 30 55fg 40"))

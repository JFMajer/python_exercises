def my_sum(*nums):
    sum_to_return = 0
    for num in nums:
        sum_to_return += num
    return sum_to_return


print(my_sum(1, 3, 6))

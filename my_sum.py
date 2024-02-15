def my_sum(*sequence):
    if not sequence:
        return sequence
    output = sequence[0]
    for ele in sequence[1:]:
        output += ele
    return output


print(my_sum('abc', 'efg'))
print(my_sum([1,2,3], [4,5,6]))
print(my_sum())
print(my_sum("a"))
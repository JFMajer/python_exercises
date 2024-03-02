PEOPLE = [('Donald', 'Trump', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]


def format_sort_records(list_of_tuples):
    list_of_tuples.sort(key=lambda a: a[1])
    output = []
    for p in list_of_tuples:
        formatted = f"{p[1]:<10}{p[0]:<10}{p[2]:>5.2f}"
        output.append(formatted)
    return '\n'.join(output)


print(format_sort_records(PEOPLE))

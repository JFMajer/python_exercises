def flatten_old(list1: list) -> list:
    to_return = []
    for ele in list1:
        if isinstance(ele, list):
            for nested_ele in ele:
                to_return.append(nested_ele)
        else:
            to_return.append(ele)
    return to_return


def flatten(list1: list) -> list:
    to_return = [one_element for one_sublist in list1 for one_element in one_sublist]

    return to_return

    # for one_sublist in list1:
    #     for one_element in one_sublist:
    #         to_return.append(one_element)


list2 = flatten([[1, 2], [3, 4]])
print(list2)

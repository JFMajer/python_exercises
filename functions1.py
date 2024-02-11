def build_person(first_name, last_name, age=None):
    person = {"first": first_name, "last": last_name}
    if age:
        person['age'] = age

    return person


print(build_person("jimmy", "hendrix"))
print(build_person("elvis", "presley", 47))


def make_pizza(size, *toppings):
    print(f"making a {size}-inch pizza with following toppings: ")
    for t in toppings:
        print(f" - {t}")


make_pizza(16, "mushrooms")
make_pizza(24, "mushrooms", "apples", "tuna")

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein', university='princeton', field='physics')
print(user_profile)
MENU = {
    "sandwich": 10,
    "coffee": 2.5,
    "soup": 5,
    "fries": 3
}

order = {}
total = 0
while True:
    item = input("Order: ")
    if not item:
        break
    if item in MENU:
        if item in order:
            order[item] += MENU[item]
        else:
            order[item] = MENU[item]
        total += MENU[item]
        print(f"{item} costs {MENU[item]}, total is {total}")
    else:
        print(f"Sorry, we are fresh out of {item} today.")

print(f"Your total is {total}")
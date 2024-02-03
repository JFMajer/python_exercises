def hex_output():

    dec_number = 0
    user_input = input("Enter hex number: ")
    for i, letter in enumerate(reversed(user_input)):
        dec_number += int(letter, 16) * (16 ** i)


    print(f"result is {dec_number}")

hex_output()
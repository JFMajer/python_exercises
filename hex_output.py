from typing import Optional


def hex_output(hex_number: str) -> Optional[int]:
    dec_number = 0

    try:
        for i, letter in enumerate(reversed(hex_number)):
            dec_number += int(letter, 16) * (16 ** i)
    except ValueError:
        print(f"Error: '{letter}' is not a valid hexadecimal digit.")
        return None

    return dec_number


user_input = input("Enter hex number: ")
result = hex_output(user_input)

if result is None:
    print("Invalid hexadecimal input.")
else:
    print(f"Result of conversion is {result}")

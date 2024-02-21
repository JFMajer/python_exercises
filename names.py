from name_function import get_formatted_name

print("Enter 'q' to exit at any time.")
while True:
    first = input("\nPlease give me your first name: ")
    if first == 'q':
        break
    last =  input("\nPlease give me your last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")
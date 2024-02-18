from pathlib import Path
from colorama import Fore

while True:
    birthdate = input("please provide your birthdate in format ddmmyy: ")
    if len(birthdate.strip()) == 6 and birthdate.isdigit():
        print(f"Entered birthday is {birthdate.strip()}")
        break
    else:
        print("Please provide 6 digits")

path = Path('one_million_digits.txt')

content = path.read_text()

index = content.find(birthdate.strip())

if index != -1:
    print("Success! Your birthday appears in first one million digits of PI")
    start_pos = max(0, index-15)
    end_pos = index + len(birthdate.strip()) + 15

    surrounding_digits = content[start_pos:index] + Fore.CYAN + content[index:index+len(birthdate.strip())] + Fore.RESET + content[index+len(birthdate.strip()):end_pos]
    print(f"Surrounding digits: {surrounding_digits}")
else:
    print("Sorry, your birthdate doesn't seem to be in first one million digits of PI")

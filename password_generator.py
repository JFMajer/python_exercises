import random
from typing import Callable


def create_password_generator(characters: str) -> Callable[[int], str]:
    def inner_function(length: int) -> str:
        random_chars = [random.choice(characters) for _ in range(length)]
        return ''.join(random_chars)

    return inner_function


alpha_password = create_password_generator('abcdef')
symbol_password = create_password_generator('!@#$%')
print(alpha_password(5))
 # efeaa
print(alpha_password(10))
 # cacdacbada
print(symbol_password(5))
 # %#@%@
print(symbol_password(10))
 # @!%%$%$%%#
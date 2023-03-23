from string import ascii_letters, digits, punctuation
from random import choice, shuffle


def generate_password(length: int, use_symbols=True):
    if length < 4:
        raise ValueError("A senha deve ter pelo menos 4 caracteres")

    lower = choice(ascii_letters.lower())
    upper = choice(ascii_letters.upper())
    digit = choice(digits)
    symbol = choice(punctuation) if use_symbols else ""

    required_chars = [lower, upper, digit, symbol]
    shuffle(required_chars)

    remaining_length = length - len(required_chars)
    all_character = ascii_letters + digits + (punctuation if use_symbols else "")
    remaining_chars = [choice(all_character) for _ in range(remaining_length)]

    password = remaining_chars + required_chars
    shuffle(password)

    return "".join(password)


def get_user_input():
    length = int(input("How long would you like your password to be: "), base=10)

    while True:
        use_symbols = input("Would you like to use symbols Y/n: ").lower() or "y"

        if use_symbols in ["y", "n"]:
            break

    use_symbols = True if use_symbols == "y" else False

    return length, use_symbols


if __name__ == "__main__":
    length, use_symbols = get_user_input()

    password = generate_password(length, use_symbols)

    print(f"{password=}")

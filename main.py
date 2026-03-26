def is_very_long(password):
    return len(password) < 12


def has_digit(password):
    return any(char.isdigit() for char in password)


def has_upper_letters(password):
    return any(char.isupper() for char in password)


def has_lower_letters(password):
    return any(char.islower() for char in password)


def has_symbols(password):
    return any(not char.isalpha() and not char.isdigit() for char in password)


def main():
    user_password = input("Введите пароль: ")
    is_very_long_check = is_very_long(user_password)
    has_digit_check = has_digit(user_password)
    has_upper_letters_check = has_upper_letters(user_password)
    has_lower_letters_check = has_lower_letters(user_password)
    has_symbols_check = has_symbols(user_password)
    password_checks = [
        is_very_long_check,
        has_digit_check,
        has_upper_letters_check,
        has_lower_letters_check,
        has_symbols_check,
    ]
    score = 0
    for check in password_checks:
        if check:
            score = score + 2
    print(f"Рейтинг пароля: {score}")


if __name__ == "__main__":
    main()

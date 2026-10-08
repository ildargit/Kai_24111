import random
import string


def get_choice(input_text):
    while True:
        choice = input(input_text).strip().lower()
        if choice in ("y", "n", ""):
            return choice in ("y", "")
        print("Пожалуйста, введите 'y' или 'n'.")


def main():
    while True:
        try:
            length = int(input("Введите желаемую длину пароля: "))
            if length <= 0:
                print("Длина должна быть положительным числом.")
                continue
            break
        except ValueError:
            print("Пожалуйста, введите целое число.")

    use_lower = get_choice("Использовать строчные буквы? (Y/n): ")
    use_upper = get_choice("Использовать заглавные буквы? (Y/n): ")
    use_digits = get_choice("Использовать цифры? (Y/n): ")
    use_symbols = get_choice("Использовать спецсимволы? (Y/n): ")

    pools = []
    if use_lower:
        pools.append(string.ascii_lowercase)
    if use_upper:
        pools.append(string.ascii_uppercase)
    if use_digits:
        pools.append(string.digits)
    if use_symbols:
        pools.append(string.punctuation)

    if not pools:
        print("Не выбран ни один тип символов. Невозможно создать пароль.")
        return

    if length < len(pools):
        print(
            f"Длина пароля должна быть не меньше {len(pools)}, чтобы включить все выбранные типы символов."
        )
        return

    all_chars = "".join(pools)
    password_chars = [random.choice(pool) for pool in pools]
    remaining = length - len(password_chars)
    password_chars.extend(random.choice(all_chars) for _ in range(remaining))
    random.shuffle(password_chars)
    password = "".join(password_chars)

    print(f"Сгенерированный пароль: {password}")


main()

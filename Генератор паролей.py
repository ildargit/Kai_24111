import random
import string


def generate_password():
    print("Добро пожаловать в Генератор Надежных Паролей")

    while True:
        try:
            length = int(input("Введите длину пароля: "))
            if length < 1:
                print("Длина пароля должна быть не менее 1 символа.")
                continue
            break
        except ValueError:
            print("Пожалуйста, введите корректное число.")

    print("\nНастройте параметры пароля:")
    use_lowercase = get_boolean_input("Использовать строчные буквы (a-z)? (y/n): ")
    use_uppercase = get_boolean_input("Использовать заглавные буквы (A-Z)? (y/n): ")
    use_digits = get_boolean_input("Использовать цифры (0-9)? (y/n): ")
    use_punctuation = get_boolean_input("Использовать спецсимволы (!, @, #...)? (y/n): ")

    selected_pools = {}
    if use_lowercase:
        selected_pools['lowercase'] = string.ascii_lowercase
    if use_uppercase:
        selected_pools['uppercase'] = string.ascii_uppercase
    if use_digits:
        selected_pools['digits'] = string.digits
    if use_punctuation:
        selected_pools['punctuation'] = string.punctuation

    if not selected_pools:
        print("\nОшибка: Вы должны выбрать хотя бы один тип символов! Автоматически включаем строчные буквы.")
        selected_pools['lowercase'] = string.ascii_lowercase

    password_chars = []

    # Если запрашиваемая длина позволяет вместить все выбранные пулы
    if length >= len(selected_pools):
        for pool in selected_pools.values():
            password_chars.append(random.choice(pool))

        all_allowed_chars = "".join(selected_pools.values())
        remaining_length = length - len(password_chars)
        for _ in range(remaining_length):
            password_chars.append(random.choice(all_allowed_chars))

        random.shuffle(password_chars)
    else:
        # Если длина (например, 1) меньше, чем количество выбранных категорий,
        # мы просто берем случайные символы из общего списка разрешенных символов
        all_allowed_chars = "".join(selected_pools.values())
        for _ in range(length):
            password_chars.append(random.choice(all_allowed_chars))

    final_password = "".join(password_chars)

    print("\n" + "=" * 40)
    print(f" Ваш пароль: {final_password}")
    print("=" * 40)


def get_boolean_input(prompt):
    while True:
        choice = input(prompt).strip().lower()
        if choice in ['y', 'yes', 'д', 'да']:
            return True
        if choice in ['n', 'no', 'н', 'нет']:
            return False
        print("Пожалуйста, ответьте 'да' или 'нет' (y/n).")


if __name__ == "__main__":
    generate_password()

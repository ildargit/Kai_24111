import secrets
import string

# Набиуллин Азамат 24111 2026 Проект 2


def main() -> None:
    length = -1
    while length == -1:
        try:
            length = int(input("Длина пароля: "))
        except ValueError:
            print("Длина пароля должна быть целым числом! Попробуйте еще раз")

    symbol_types = [string.ascii_lowercase]
    alphabet = string.ascii_lowercase
    print("Какие символы использовать при генерации пароля?")
    if input("Заглавные буквы? Y/N: ") == "Y":
        symbol_types.append(string.ascii_uppercase)
        alphabet += string.ascii_uppercase
    if input("Цифры? Y/N: ") == "Y":
        symbol_types.append(string.digits)
        alphabet += string.digits
    if input("Специальные символы? Y/N: ") == "Y":
        symbol_types.append(string.punctuation)
        alphabet += string.punctuation

    password = ""
    while True:
        for i in range(length):
            password += secrets.choice(alphabet)

        # Проверяем имеется ли в пароле хотя бы один символ каждого типа
        success = True
        for symbol_type in symbol_types:
            success = success and any(char in password for char in symbol_type)

        if success:
            break

    print(f"Сгенерированый пароль: {password}")


if __name__ == "__main__":
    main()

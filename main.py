import os
from cryptography.fernet import Fernet


def write_key():
    if not os.path.exists('key.key'):
        key = Fernet.generate_key()
        with open('key.key', 'wb') as file:
            file.write(key)


def load_key():
    with open('key.key', 'r') as file:
        key = file.read()
    return key
    

def add(f):
    login = input('Логин: ')
    password = input('Пароль: ')
    encrypted_password = f.encrypt(password.encode()).decode()
    with open('passwords.txt', 'a') as file:
        file.write(f'{login}|{encrypted_password}\n')
    print('Успешно')


def view(f):
    with open('passwords.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.rstrip('\n')
            login, password = line.split('|')
            password = f.decrypt(password.encode()).decode()
            print(f'Логин: {login} | Пароль: {password}')


def main():
    write_key()
    key = load_key()
    f = Fernet(key)
    while True:
        print('Выберите функцию:\n0. Выход.\n1. Добавить пароль.\n2. Посмотреть пароли.\n')
        choice = int(input('0 / 1 / 2: '))
        if choice == 0:
            break
        elif choice == 1:
            add(f)
        elif choice == 2:
            view(f)
        else:
            print('Неверный ввод')


if __name__ == '__main__':
    main()
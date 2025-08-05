from cryptography.fernet import Fernet
from main import load_key


def authorization(login, password, f):
    with open('passwords.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.rstrip('\n')
            true_login, true_password = line.split('|')
            true_password = f.decrypt(true_password.encode()).decode()
            if login == true_login and password == true_password: return True
        return False
            

def main():
    key = load_key()
    f = Fernet(key)
    while True:
        login = input('Логин: ')
        password = input('Пароль: ')
        if not authorization(login, password, f): 
            print('Неверное имя пользователя или пароль.')
        else: 
            print('Успешная авторизация.')
            break


if __name__ == '__main__':
    main()
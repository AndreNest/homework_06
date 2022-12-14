import random
def generate_password(m):
    ascii_letters = 'abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'
    password = []
    for i in range(m):
        password.append(ascii_letters[random.randint(0, len(ascii_letters) - 1)])
    return password

def main(n,m):
    list_password = []
    for i in range(n):
        list_password.append(generate_password(m))
    for j in list_password:
        print(''.join(j))
main(int(input('Сколько будет паролей?: ')), int(input('Сколько будет символов в пароле?: ')))
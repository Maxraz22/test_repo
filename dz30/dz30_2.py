import hashlib

autorize = dict()
login1 = input("Оберіть Ваш логін: ")
passwd1 = input("Введіть Ваш пароль: ")

while True:
    login2 = input("Оберіть Ваш логін: ")
    if login2 == login1:
        print("Такий логін вже існує!")
    else:
        passwd2 = input("Введіть Ваш пароль: ")
        break

while True:
    login3 = input("Оберіть Ваш логін: ")
    if login3 == login2 or login3 == login1:
        print("Такий логін вже існує!")
    else:
        passwd3 = input("Введіть Ваш пароль: ")
        break

passwd_hash1 = hashlib.md5(bytes(passwd1, 'UTF-8'))
passwd_hash2 = hashlib.md5(bytes(passwd2, 'UTF-8'))
passwd_hash3 = hashlib.md5(bytes(passwd3, 'UTF-8'))
print(passwd_hash1.hexdigest())
print(passwd_hash2.hexdigest())
print(passwd_hash3.hexdigest())

autorize[login1] = passwd_hash1.hexdigest()
autorize[login2] = passwd_hash2.hexdigest()
autorize[login3] = passwd_hash3.hexdigest()

print(autorize)

my_login = input("Введіть Ваш логін: ")
my_passwd = input("Введіть Ваш пароль: ")
my_passwd_hash = hashlib.md5(bytes(my_passwd, 'UTF-8'))
print(my_passwd_hash.hexdigest())

if my_passwd_hash.hexdigest() == autorize['Ivanenko']:
        print("ВИ АВТОРИЗОВАНІ!")
elif my_passwd_hash.hexdigest() == autorize['Petrenko']:
        print("ВИ АВТОРИЗОВАНІ!")
elif my_passwd_hash.hexdigest() == autorize['Sydorenko']:
        print("ВИ АВТОРИЗОВАНІ!")
else:
        print("Невірний логін/пароль!")

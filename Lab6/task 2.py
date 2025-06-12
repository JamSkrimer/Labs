class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def __str__(self):
        return f'{self.login} {self.password}'

user = [
    User('admin', 'admin'),
    User('vorker404', 'asddqd123e1'),
    User('lits', 'fbdfjvsdfhj1231414'),
]

num = input('Выведите Юзеара: ')
found = [t for t in user if t.login == num]
print(found[0] if found else "Юзера такого нема")
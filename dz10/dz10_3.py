# Функціонал власного класу виключення при розміщенні домашнього завдання на GitHub
class MyCustomError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('calling str')
        if self.message:
            return f'MyCustomError, {self.message}'
        else:
            return 'MyCustomError has been raised'


class GitHub(MyCustomError):
    def repo(self, dz):
        self.send_dz(dz)
        print(f'Send to GitHub: {dz}')

    def send_dz(self, dz):
        if not self.upload_repo(dz):
            raise MyCustomError('We have a problem')

    def upload_repo(self, dz):
        return False


ex = GitHub()
try:
    ex.repo('file dz10.py')
except MyCustomError:
    print('We have a problem')



class File:
    def __init__(self):
        print(f'вызвали __init__')

    def __enter__(self):
        print('вызвали __enter__')

    def __exit__(self, exc_type, exc_value, traceback):
        print('вызвали __exit__')


with File():
    print('вызвали ваш блок кода в with')


class File:
    def __init__(self, text):
        self.text = text

    def __enter__(self):
        return f'{self.text} и __enter__'

    def __exit__(self, exc_type, exc_value, traceback):
        print('вызвали __exit__')

sample = File('ваш текст')
with sample as method_enter:
    print(method_enter)  # ваш текст и __enter__


'''
class File:
    def __init__(self, text):
        self.text = text

    def __enter__(self):
        return f'{self.text} и __enter__'

    def __exit__(self, exc_type, exc_value, traceback):
        print(f'exc_type = {exc_type}')  # exc_type = <class 'ZeroDivisionError'>
        print(f'exc_value = {exc_value}')  # exc_value = division by zero
        print(f'traceback = {traceback}')  # traceback = <traceback object at 0x00000201D24BDE00>
        return True  # При True вывод принтов останется, принты в конт. менеджере не выполнятся

sample = File('ваш текст')
with sample as method_enter:
    print(11 / 0)
    print(method_enter)
'''


class Resource:
    def __init__(self, name):
        print('Resource: create {}'.format(name))
        self.__name = name
    def get_name(self):
        return self.__name
    def post_work(self):
        print('Resource: close')


class ResourceForWith:
    def __init__(self, name):
        self.__resource = Resource(name)
    def __enter__(self):
        return self.__resource
    def __exit__(self, type, value, traceback):
        self.__resource.post_work()

with ResourceForWith('Worker') as r:
    print(r.get_name())



'''
planetes = ['Сатурн', 'Юпитер', 'Земля', 'Марс']


class StarTravel:

    def __init__(self, other):
        planetes.append(other)

    def __enter__(self):
        return planetes

    def __exit__(self, exc_type, exc_value, traceback):
        print('Венера')
        return True


# код ниже пожалуйста не меняйте
with StarTravel('Плутон') as word:
    [print(i) for i in word]
'''
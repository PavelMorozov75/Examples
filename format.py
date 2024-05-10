
class MyClass:
    def __init__(self, url):
        self.url = url

    def get_url(self, path):
        return '{0}/{1}'.format(self.url, path.strip('/'))

obj = MyClass('http://www.example.com')
print(obj.get_url('/test/path/'))



def format_float_to_string(num):
    """Перевод float в str"""
    return "{:,.2f}".format(num).replace(",", " ").replace(".", ",")


# :запускает спецификацию формата.
# ,используется как разделитель тысяч.
# .2f - указывает, что число должно быть отформатировано двумя цифрами после десятичной точки.



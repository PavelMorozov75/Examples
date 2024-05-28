from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Union
import time


class BasePage:

    by = selector = None
    driver = None
    _url = ""



    def __init__(self, driver = None):
        self._base_url: str = ""
        if driver:
            if not isinstance(driver, WebDriver):
                raise TypeError('В класс страницы передан не драйвер, а %s' % type(driver))
            self.driver: WebDriver = driver
            self._base_url = "https://qa-scooter.praktikum-services.ru/"
            # self.browser: Browser = Browser(driver)
            self.init()

    def get_elements(self) -> tuple:
        """Получение потенциально элементов из класса
         нужен из-за того что dir вычисляет свойства, а нам нужны только атрибуты класса"""

        for _class in self.__class__.__mro__:
            print('_class mro', _class)
            for key, value in _class.__dict__.items():
                if not key.startswith('_') and not isinstance(getattr(self.__class__, key), property):
                    value = getattr(self, key)
                    if isinstance(value, (HtmlElement, BasePage)):
                        # print('key ', key, 'value ', value)
                        yield key, value

    def init(self):
        """Инициализация класса когда передали driver"""

        for key, cur_value in self.get_elements():
            if isinstance(cur_value, HtmlElement):
                try:
                    setattr(self, key, cur_value.new_instance(driver=self.driver, page=self, name=key))
                    # print('self', self, key, cur_value)
                except Exception as error:
                    raise type(error)(f'Не смогли создать копию элемента\n'
                                      f'key: {key}\n'
                                      f'type: {type(cur_value)}\n'
                                      f'{repr(error)}')
            elif isinstance(cur_value, BasePage):
                print('1111')
                cur_value.__init__(self.driver)
        print(self, self.__dict__)

        # PageDecorator.set_grid(self)

class HtmlElement:
    """Base element"""

    driver: WebDriver = None
    absolute_position = None

    def __str__(self):
        return self.__class__.__name__

    def __init__(self, by_type: str, selector: Union[str, tuple], name: str = "", **kwargs):
        self._by = by_type
        if by_type is not None:
            self._by_selector = selector
        self.driver: WebDriver = kwargs.get("driver", None)
        self.parent = kwargs.get("parent")
        self.page = kwargs.get("page")
        self._name = name if name else self.__str__()
        self._find_element = None
        self._kwargs = tuple(kwargs.items())
        if kwargs.get("absolute_position"):
            self.absolute_position = kwargs.get("absolute_position")
        if self.driver:
            self.init(self.driver)

    def init(self, driver: WebDriver, parent=None, page=None, name='') -> None:
        """Инициализация элементов"""

        self.driver = driver
        self.parent = self.page = None
        if name:
            self._name = name
        if not self.absolute_position:
            self.page = page

            if not (self.parent and parent is None):
                self.parent = parent
                if parent and page is None:
                    self.page = parent.page

        self.create_child_items()
        if self.absolute_position:
            pass

    def get_elements(self):
        for key, value in self.__dict__.items():
            if key not in ("page", "parent"):
                yield key, value

    def create_child_items(self):
        """Создать дочерние элементы"""

        for key, value in self.get_elements():
            if issubclass(value.__class__, HtmlElement):
                value.init(self.driver, parent=self, page=self.page)


    def new_instance(self, driver, parent=None, page=None, name=''):
        """Получение нового экземпляра элемента"""

        if self._kwargs:
            new_item = type(self)(self._by, self._by_selector, self._name,
                                  **{k: v for k, v in self._kwargs})
        else:
            new_item = type(self)(self._by, self._by_selector, self._name)
        new_item.init(driver, parent=parent or self.parent, page=page)
        # print('new_item ', new_item)

        return new_item

class Page(BasePage):

    def __init__(self, driver):
        # self.url = url
        self.driver = driver
        super().__init__(driver)

    aa = HtmlElement(By.XPATH, "(//button[contains (@class, 'Button_Button')])[1]")

    @property
    def get_base_url(self):
        self.driver.get(self._base_url)

class Page1(Page):
    def __init__(self, driver, url):
        self.url = url
        self.driver = driver
        super().__init__(driver)





driver = webdriver.Chrome()
url = "https://qa-scooter.praktikum-services.ru/"
page = Page(driver)
page.get_base_url
page.get_elements()
# print(page.__dict__)
# print(page.aa)
# print(page.aa.page)
# print(page.aa.parent)

page1 = Page1(driver, url)
time.sleep(1)



driver.quit()



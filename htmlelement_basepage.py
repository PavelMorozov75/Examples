from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Union
driver = webdriver.Chrome()

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
            self._base_url = "https://stellarburgers.nomoreparties.site/register"
            # self.browser: Browser = Browser(driver)
            self.init()

    def get_elements(self) -> tuple:
        """Получение потенциально элементов из класса
         нужен из-за того что dir вычисляет свойства, а нам нужны только атрибуты класса"""

        for _class in self.__class__.__mro__:
            for key, value in _class.__dict__.items():
                if not key.startswith('_') and not isinstance(getattr(self.__class__, key), property):
                    value = getattr(self, key)
                    if isinstance(value, (HtmlElement, BasePage)):
                        yield key, value

    def init(self):
        """Инициализация класса когда передали driver"""

        for key, cur_value in self.get_elements():
            if isinstance(cur_value, HtmlElement):
                try:
                    setattr(self, key, cur_value.new_instance(driver=self.driver, page=self, name=key))
                except Exception as error:
                    raise type(error)(f'Не смогли создать копию элемента\n'
                                      f'key: {key}\n'
                                      f'type: {type(cur_value)}\n'
                                      f'{repr(error)}')
            elif isinstance(cur_value, BasePage):
                cur_value.__init__(self.driver)

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
            self.set_name(name)
        if not self.absolute_position:
            self.page = page

            if not (self.parent and parent is None):
                self.parent = parent
                if parent and page is None:
                    self.page = parent.page

        self.create_child_items()
        if self.absolute_position:
            pass

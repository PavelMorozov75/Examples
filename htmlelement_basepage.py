from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Union
import time
from typing import List, Dict, Tuple
from selenium.webdriver.remote.webdriver import WebElement
from typing import Union, Any, Callable, Type, List, Type

from selenium.common.exceptions import WebDriverException, NoSuchElementException, StaleElementReferenceException

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

        print(self.__class__.__mro__)
        for _class in self.__class__.__mro__:
            # print(self, self.__class__)
            # print('_class mro', _class)
            #print(_class.__dict__.items())
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
                    pass
                except Exception as error:
                    raise type(error)(f'Не смогли создать копию элемента\n'
                                      f'key: {key}\n'
                                      f'type: {type(cur_value)}\n'
                                      f'{repr(error)}')
            elif isinstance(cur_value, BasePage):
                # print('1111')
                # print(cur_value)
                cur_value.__init__(self.driver)
                # cur_value.__init__()
        # print(self, self.__dict__)

        # PageDecorator.set_grid(self)

    def parent_func(self):
        if self.by:
            return DefaultSelector(self.by, self.selector)

def find_elements(by_type: str, locator: str, webelement: WebElement) -> List[WebElement]:
    """Поиск элементов в других элементах

    :param by_type: стратегия поиска
    :param locator: локатор
    :param driver: драйвер
    :param webelement: если ищем в родительском элементе
    """

    elements = webelement.find_elements(by_type, locator)

    return elements


def convert_to_css(by: str, selector: str) -> Tuple[str, str]:
    """Конвертируем в css"""

    templates: Dict[str, Tuple[str, str]] = {
        By.ID: (By.CSS_SELECTOR, '[id="{0}"]'),
        By.NAME: (By.CSS_SELECTOR, '[name="{0}"]'),
        By.CLASS_NAME: (By.CSS_SELECTOR, '.{0}'),
    }
    res = templates.get(by)
    if res:
        how, template = res
        selector = template.format(selector)
    return by, selector

class DefaultSelector:

    def __str__(self):
        return f'{self.by_type}: {self.selector}'

    def __init__(self, by_type, selector):
        self.by_type, self.selector = convert_to_css(by_type, selector)

    def __call__(self, driver, webelement):
        if self.selector:
            return find_elements(self.by_type, self.selector, webelement)
        else:
            return [driver, ]


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
        # print('Это оно   : ', self.driver)
        # print(self)
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
        # print(parent, page, driver)
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
                # print('key ', key)
                # print('value ', value)
                yield key, value

    def create_child_items(self):
        """Создать дочерние элементы"""

        for key, value in self.get_elements():
            # print('value', value, type(value), 'key ', key)
            # print('value.__class__', value.__class__)
            if issubclass(value.__class__, HtmlElement):
                print('создан дочерний элемент')
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

    @property
    def find_element(self):
        if not self._find_element:
            self._find_element = DefaultSelector(self._by, self._by_selector)
        return self._find_element

    @find_element.setter
    def find_element(self, value):
        self._find_element = value

        def add_parent(self, parent_element: 'HtmlElement') -> None:
            """Добавляет родителя к текущему элементу
            :param parent_element: HtmlElement
            """

            self.init(parent_element.driver, parent_element, page=parent_element.page)

    def add_parent(self, parent_element: 'HtmlElement') -> None:
        """Добавляет родителя к текущему элементу
        :param parent_element: HtmlElement
        """

        self.init(parent_element.driver, parent_element, page=parent_element.page)

    @property
    def webelements(self) -> list:
        """Получение списка элементов"""



        elements_list = [self.find_element]
        parent = self.parent
        while parent:
            elements_list.append(parent.find_element)
            parent = parent.parent
            if not parent:
                break

        if self.page and isinstance(self.page, BasePage):
            func = self.page.parent_func()
            if func:
                elements_list.append(func)
        return elements_list[::-1]

    def element(self, by: str, selector: str = None, element_type = None):
        """Получить дочерний элемент"""

        if selector is None:
            selector = by
            by = By.CSS_SELECTOR

        element_type = HtmlElement if element_type is None else element_type
        child_element = element_type(by_type=by,
                                     selector=selector,
                                     name=self._name)
        child_element.add_parent(self)

        return child_element

    def webelement(self, methods_list=None, return_list: bool = False) -> Any:
        """Поиск webelement на странице"""

        if not methods_list:
            methods_list = self.webelements

        webelements = []
        end_time = time.time() + 20
        while True:
            assert self.driver, 'Не передан драйвер элементу'
            current_webelement = self.driver
            for method in methods_list:
                try:
                    webelements = method(self.driver, current_webelement)
                    if webelements and len(webelements) > 0:
                        current_webelement = webelements[0]
                        continue
                    else:
                        break
                except WebDriverException:
                    break
            else:
                break

            if time.time() > end_time:
                raise NoSuchElementException(f'no such element: Unable to locate element: '
                                             f'{{"method":"{self._by}","selector":"{self._by_selector}"}}')
        return webelements if return_list else webelements[0]



class HtmlList(HtmlElement):
    nn = HtmlElement(By.CSS_SELECTOR, "(//button[contains (@class, 'Button_Button@@@@@')])[1]")



class Page(BasePage):

    def __init__(self, driver):
        # self.url = url
        self.driver = driver
        self.jj = 9
        super().__init__(driver)
        self.aa = HtmlElement(By.CSS_SELECTOR, "(//button[contains (@class, 'Button_Button@@@@@')])[1]", driver=self.driver )

    kk = HtmlElement(By.XPATH, "(//button[contains (@class, 'Button_Button')])[1]")
    kk1 = HtmlList(By.XPATH, "(//button[contains (@class, 'Button_Button')])[1]111")


    cc = 555

    @property
    def get_base_url(self):
        self.driver.get(self._base_url)




class Page1(Page):


    def __init__(self, driver, url):
        self.url = url
        self.driver = driver
        super().__init__(driver)
        self.bb = BasePage()
        self.iii()
        self.pp = HtmlList(By.XPATH, "(//button[contains (@class, 'Button_Button')])[1]333", driver=self.driver)



    def iii(self):
        ll = BasePage()
        return ll #не инициализирует, так как не аттрибут класса

    uu = BasePage()#А вот сюда передаст драйвер и инициализирует
    hh = HtmlElement(By.XPATH, "(//button[contains (@class, 'Button_Button')])[1]")
    dd = HtmlList(By.XPATH, "(//button[contains (@class, 'Button_Button')])[1]")


driver = webdriver.Chrome()
url = "https://qa-scooter.praktikum-services.ru/"
#page = Page(driver)

# print(page.jj)
# page.get_base_url
# page.get_elements()
page1 = Page1(driver, url)

# print(page.__dict__)
# print(page.aa)
# print(page.aa.page)
# print(page.aa.parent)
# print(Page.__dict__)
ll = BasePage(driver)
listt = HtmlList(By.CSS_SELECTOR, "(//button[contains (@class, 'Button_Button')])[1]333", driver=driver)
time.sleep(1)
# print(page.__dict__)
print(page1.__dict__)
print(listt.__dict__)
# print(Page1.uu.driver)
# print(page1.bb.driver)
# print(page.aa.find_element)
# print(page.kk.find_element)
# print(page1.pp.find_element)
# print(page.kk.webelements)

driver.quit()


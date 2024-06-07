import io
import shutil
import time
from typing import Literal


import pytest
import requests



from selenium.webdriver.remote.webdriver import WebDriver



class TestCase:

    @classmethod
    @pytest.fixture(scope="class", autouse=True)
    def _base_setup_class(cls, request, app_session):

        cls._setup_cls(request, app_session=app_session)
        cls.setup_cls()
        request.addfinalizer(cls.teardown_cls)
        request.addfinalizer(lambda: cls._teardown_cls(request))

    @pytest.fixture(autouse=True)
    def _base_setup(self, request):
        """base method for call teardown after failed setup"""

        request.addfinalizer(self.tear_down)
        request.addfinalizer(lambda: self._teardown(request))

    @classmethod
    def _setup_cls(cls, request, **kwargs):
        """framework setup"""
        print('Framework setup  ')
        # cls.config: Config = Config()
        # if request.config.getoption("--stand"):
        #     cls.config.set("BASE_URL", request.config.getoption("--stand"), "GENERAL")
        # cls.client = ApiClient(cls.config.get("BASE_URL", "GENERAL"), session=kwargs.get("app_session"))
        # if cls.config.get("CHECK_SERVICE_AVAILABLE", "GENERAL"):
        #     cls.wait_available()

    @classmethod
    def setup_cls(cls):
        """action suite"""

    def set_up(self):
        """action test"""

    def tear_down(self):
        """action test"""

    def _teardown(self, request):
        pass

    @classmethod
    def _teardown_cls(cls, request):
        """framework teardown"""

    @classmethod
    def teardown_cls(cls):
        """action suite"""


class Test1(TestCase):

    @classmethod
    def setup_cls(cls):
        print('сетап класса')

    def set_up(self):
        print('setup test')
    def test_111(self):
        print('Первый тест')

    def test_222(self):
        print('Второй тест')

    def tear_down(self):
        print('teardown_test')


    @classmethod
    def teardown_cls(cls):
        print('teardown cls')

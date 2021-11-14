# import pytest
# import yaml
# import allure
# class TestDemo:
#     @pytest.fixture(autouse=True)
#     def open(self):
#         print('打开浏览器')
#     def fun(self, x):
#         return x
#
#     def test_pytest1(self,login):
#         print('测试一下')
#         assert(self.fun(3) == 3)
#         print('我们都有一个家，名字叫中国')
#
#     def test_pytest2(self,login):
#         assert self.fun(4) == 4
#
#     def test_pytest3(self):
#        # print(yaml.safe_load(open("./data.yaml")))
#         assert self.fun(5) == 5
#
# class TestFemo1:
#     def fun(self, x):
#         return x
#
#     def test_pytest1(self):
#         assert self.fun(3) == 3
#
#     def test_pytest2(self):
#         assert self.fun(4) == 4
#
#     def test_pytest3(self):
#         assert self.fun(5) == 5
#
#
import pytest

pytest
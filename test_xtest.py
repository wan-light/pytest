# import pytest
# import yaml
#
# class TestData:
#     @pytest.mark.parametrize("a,b",yaml.safe_load(open("./data.yaml")))
#     def test_data(self,a,b):
#         print(a+b)
#
#     def test_fix(self):
#         pass
# -*- coding:utf-8 -*-
'''
@Time       : 2020/12/28 19:56
@Author     : 测试工程师Jane
@FileName   : g.py
@Description:
'''

import pytest
# fixture作用域 scope = 'class'
@pytest.fixture(scope='class')
def login():
    print("scope为class")
class TestLogin:
    def test_1(self, login):
        print("用例1")

    def test_2(self):
        print("用例2")

    def test_3(self, login):
        print("用例3")


if __name__ == '__main__':
    pytest.main()

import pytest
class TestDemo:
    def fun(self, x):
        return x

    def test_pytest1(self):
        print('测试一下')

        pytest.assume(self.fun(3) == 6)
        pytest.assume(self.fun(3) == 4)
        pytest.assume(self.fun(5) == 7)

        print('我们都有一个家，名字叫中国')

    def test_pytest2(self):
        assert self.fun(4) == 4

    def test_pytest3(self):
        assert self.fun(5) == 5

class TestFemo1:
    def fun(self, x):
        return x

    def test_pytest1(self):
        assert self.fun(3) == 3

    def test_pytest2(self):
        assert self.fun(4) == 4

    def test_pytest3(self):
        assert self.fun(5) == 5
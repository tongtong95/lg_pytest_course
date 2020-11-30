# -*- coding: utf-8 -*-
# @Time    : 2020/11/30 11:36
# @Author  : tongtong
# @File    : test_calc.py
# @Software: Pycharm
import pytest

from test_pytest.core.calc import Calc


class TestCalc:
    # # 类的初始化，方法二：每次都会被执行，不推荐
    # def setup(self):
    #     self.calc = Calc()

    # 类的初始化，方法三：类初始化时只会被执行一次，推荐方法
    def setup_class(self):
        self.calc = Calc()

    # pytest的mark方法，可以实现测试用例的参数化功能.
    # 前边是参数，后边是传入的数据
    # 乘法测试用例
    @pytest.mark.parametrize('a, b, c', [
        # 整数
        [1, 2, 2],
        [2, 9, 18],
        [-1, -2, 2],
        [-1, 2, -2],
        [2, -2, -4],
        [999999, 999999, 999998000001],
        # 小数
        [0.2, 0.3, 0.06],
        [-0.2, 0.3, -0.06],
        [0.2, -0.3, -0.06],
        [-0.2, -0.3, 0.06],
        # 小数和整数的混合
        [2, 0.2, 0.4],
        [2, -0.2, -0.4],
        [-2, 0.2, -0.4],
        [-2, -0.2, 0.4],
        # 乘0
        [2, 0, 0],
        [0, 1, 0],
        [-2, 0, 0],
        [0, 0, 0],
        [0.1, 0, 0],
        [-0.1, 0, 0],
        [0, -0.1, 0],
        # 特殊值
        ['a', 2, 0]
    ])
    def test_mul(self, a, b, c):
        # # 类的初始化，方法一：引入不同参数，类被反复初始化，逻辑复杂时，成本比较大,不推荐
        # 多个测试用例使用同一个类，利用setup或者setup_class
        # calc = Calc()
        assert self.calc.mul(a, b) == c

    # 特殊值处理
    @pytest.mark.parametrize('a, b',[
        ['a', 'b']
    ])
    def test_mul1(self, a, b):
        with pytest.raises(TypeError):
            assert self.calc.mul(a, b)

    # 断言一定引发异常，利用with pytest.raises():
    # def test_mul_exec(self, a, b):
    # with pytest.raises()

    # 除法测试用例
    @pytest.mark.parametrize('a, b, c', [
        # 整数相除
        [2, 1, 2],
        # 0除以任何值
        [0, 2, 0],
        [0, -2, 0],
        [0, -0.1, 0],
        [0, 0.1, 0]
    ])
    def test_div(self, a, b, c):
        # # 类的初始化，方法一：引入不同参数，类被反复初始化，逻辑复杂时，成本比较大,不推荐
        # 多个测试用例使用同一个类，利用setup或者setup_class
        # calc = Calc()
        assert self.calc.div(a, b) == c

    # 除零异常值用例
    @pytest.mark.parametrize('a, b', [
        [2, 0],
        [-2, 0],
        [0.2, 0],
        [-0.2, 0],

    ])
    def test_div1(self, a, b):
        # 断言一定引发异常，利用with pytest.raises(异常类型):
        # 若不知道具体异常，可以直接写pytest.raises(Exception):
        with pytest.raises(ZeroDivisionError):
            assert self.calc.div(a, b)

    # 流程测试，先乘后除，先除后乘
    def test_process(self, a, b):
        self.calc.mul(1, 2)
        self.calc.div(3, 4)

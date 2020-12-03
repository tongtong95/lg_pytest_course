# -*- coding: utf-8 -*-
# @Time    : 2020/11/30 11:36
# @Author  : tongtong
# @File    : test_calc.py
# @Software: Pycharm
import allure
import pytest
from test_pytest.core.calc import Calc


class TestCalc:
    # # 类的初始化，方法二：每次都会被执行，不推荐
    # def setup(self):
    #     self.calc = Calc()

    # 类的初始化，方法三：类初始化时只会被执行一次，推荐方法
    # 在测试用例执行之前会先执行它
    def setup_class(self):
        self.calc = Calc()

    # 类的初始化方法四，类初始化时只会被执行一次
    # @classmethod
    # def setup_class(cls):
    #     print("setup_class classmethod")
    #     cls.calc=Calc()

    # 通过参数记录关键过程
    @allure.step
    def simple_step(self, step_param1, step_param2=None):
        pass

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
    ])
    def test_mul(self, a, b, c):
        # # 类的初始化，方法一：引入不同参数，类被反复初始化，逻辑复杂时，成本比较大,不推荐
        # 多个测试用例使用同一个类，利用setup或者setup_class
        # calc = Calc()
        # 添加附件，UI自动化测试中截图追加到报告中
        allure.attach.file('test_pytest/images/拉勾.png', "拉勾直播", allure.attachment_type.PNG)
        # 通过参数记录测试步骤中的关键过程
        self.simple_step(f'{a} {b} {c}')
        assert self.calc.mul(a, b) == c

    # 特殊值用例--类型异常
    @pytest.mark.parametrize('a, b', [
        ['a', 'b'],
        ['a', 0.3],
        ['a', -0.3]
    ])
    def test_mul1(self, a, b):
        with pytest.raises(TypeError):
            assert self.calc.mul(a, b)

    # 特殊值用例
    @pytest.mark.parametrize('a, b', [
        ['a', 0],
        ['a', -3],
    ])
    def test_mul2(self, a, b):
        with pytest.raises(Exception):
            assert self.calc.mul(a, b)

    # 特殊值用例---不懂，为什么会出来aaa的结果
    @pytest.mark.parametrize('a, b, c', [
        ['a', 3, 'aaa'],
    ])
    def test_mul2(self, a, b, c):
        assert self.calc.mul(a, b) == c

    # 除法测试用例
    @pytest.mark.parametrize('a, b, c', [
        # 整数相除为整数
        [2, 1, 2],
        [6, 2, 3],
        [6, -2, -3],
        [-6, 2, -3],
        [-6, -2, 3],
        # 整数相除为小数
        [3, 2, 1.5],
        [3, -2, -1.5],
        [-3, 2, -1.5],
        [-3, -2, 1.5],
        # 结果除不尽
        [4, 3, 1.3333333333333333],
        [4, -3, -1.3333333333333333],
        [-4, 3, -1.3333333333333333],
        [-4, -3, 1.3333333333333333],

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

    # 除零异常值用例
    @pytest.mark.parametrize('a, b', [
        ['a', 'b'],
        ['a', 3],
        ['a', -3],
        ['a', 0.2],
        ['a', -0.2],
        ['a', 0],
        [0, 'a']
    ])
    def test_div2(self, a, b):
        # 断言一定引发异常，利用with pytest.raises(异常类型):
        # 若不知道具体异常，可以直接写pytest.raises(Exception):
        with pytest.raises(TypeError):
            assert self.calc.div(a, b)

    # 流程测试，先乘后除，先除后乘
    @pytest.mark.parametrize('a, b, d, e', [
        [2, 3, 6, 1],
        [-3, 4, 6, -2]
    ])
    def test_process(self, a, b, d, e):
        c = self.calc.mul(a, b)
        assert self.calc.div(c, d) == e

# -*- coding: utf-8 -*-
# @Time    : 2020/11/30 19:45
# @Author  : tongtong
# @File    : test_fixture_demo.py
# @Software: Pycharm

import pytest
from test_pytest.core.calc import Calc


# # 可以自定义scope的范围：function，class，module，package或session
# @pytest.fixture(scope='module')
# def calc_init():
#     print("setup_class")
#     return Calc()


def test_calc_demo(calc_init):
    assert calc_init.mul(1, 2) == 2


def test_calc_demo2(calc_init):
    assert calc_init.mul(1, 3) == 3

# 不加calc_init参数，就可以不使用calc_init对应的类
def test_calc_demo3():
    assert 1 == 1

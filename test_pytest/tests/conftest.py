# -*- coding: utf-8 -*-
# @Time    : 2020/11/30 19:54
# @Author  : tongtong
# @File    : conftest.py
# @Software: Pycharm

"""
conftest.py：共享fixture功能
如果在实施测试期间要从多个测试文件中使用固定功能，则可以将其移至一个conftest.py文件中。
不需要导入要在测试中使用的fixture，它会被pytest自动发现。
fixture功能的发现顺序是测试类，测试模块，conftest.py文件，最后是内置插件和第三方插件。
如果需要跨多个类，推荐使用这种方法，一般采用setup_class和tear_down即可

每个子包里边都可以包含一个conftest



使用示例：
test_pytest/tests/test_fixture_demo.py文件的执行依赖方法def calc_init():
"""

# 可以自定义scope的范围：function，class，module，package或session
import pytest
from test_pytest.core.calc import Calc


@pytest.fixture(scope='module')
def calc_init():
    print("setup_class")
    return Calc()
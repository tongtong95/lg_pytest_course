# -*- coding: utf-8 -*-
# @Time    : 2020/12/4 10:34
# @Author  : tongtong
# @File    : test_tag.py
# @Software: Pycharm
import json

import pytest
import requests
from service.tag import Tag


# 该用例中存在的问题
# todo:代码冗余
# todo:与底层框架耦合
# todo:代码封装层次不足，get、post、参数都写在用例中，不利于后续管理

# 转成类，去管理tag下的所有用例
class TestTag:
    def setup_class(self):
        # todo:数据清理的过程，把测试数据清空或者还原
        self.tag = Tag()
        self.tag.get_token()

    # 获取企业标签库
    def test_tag_list(self):
        # 获取企业标签库
        # todo:完善功能测试
        r = self.tag.list()
        assert r.status_code == 200
        assert r.json()["errcode"] == 0

    @pytest.mark.parametrize("group_name, tag_names", [
        ["group_name_1201", [{'name': 'tag_name_1201'}]],
        ["group_name_1202", [{'name': 'tag_name_1202'}, {'name': 'tag_name_1203'}]],
    ])
    def test_tag_add(self, group_name, tag_names):
        # todo：本身数据支持参数化:利用@pytest.mark.parametrize
        # 这个类中都会使用到的初始化信息，放到setup_class(self):中
        # tag = Tag()
        # # 利用Tag类中封装的获取token的方法来获取access_token
        # tag.get_token()

        # # step1:代码中多处使用了同一变量，抽出来定义变量
        # 进一步修改：利用参数化，不直接在用例中定义变量
        # group_name = "group_name_1201"
        # tag_names = [{'name': 'tag_name_1201'}]

        # 添加企业客户标签,需要传值
        r = self.tag.add(group_name, tag_names)
        assert r.status_code == 200
        # assert r.json()["errcode"] == 0

        # 获取企业标签库,校验添加的标签是否存在
        r = self.tag.list()
        assert r.status_code == 200
        assert r.json()["errcode"] == 0

        # 校验创建的标签组和标签存在。
        """
        tag_group对应的value值是一个列表，采用for循环
        """
        group = [group for group in r.json()['tag_group'] if group['group_name'] == group_name][0]
        tags = [{'name': tag['name']} for tag in group['tag']]
        print(group)
        print(tags)
        assert group['group_name'] == group_name
        assert tags == tag_names

    # 标签名超过30个的失败
    def test_tag_add_fail(self):
        pass

# todo：课后作业：丰富标签管理的用例，主要是list、add、delete接口，完善数据清理的过程

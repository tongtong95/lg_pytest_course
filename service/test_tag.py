# -*- coding: utf-8 -*-
# @Time    : 2020/12/4 10:34
# @Author  : tongtong
# @File    : test_tag.py
# @Software: Pycharm
import json

import requests
from service.tag import Tag


# 该用例中存在的问题
# todo:代码冗余
# todo:与底层框架耦合
# todo:代码封装层次不足，get、post、参数都写在用例中，不利于后续管理


# 获取企业标签库
def test_tag_get():

    tag = Tag()
    # 利用Tag类中封装的获取token的方法来获取access_token
    tag.get_token()

    # 获取企业标签库
    r = tag.list()
    assert r.status_code == 200
    assert r.json()["errcode"] == 0

    # 代码中多处使用了同一变量，抽出来定义变量
    group_name = "group_name_1201"
    tag_names = [{'name': 'tag_name_1201'}]

    # 添加企业客户标签,需要传值
    r = tag.add(group_name, tag_names)
    assert r.status_code == 200
    # assert r.json()["errcode"] == 0

    # 获取企业标签库,校验添加的标签是否存在
    r = tag.list()
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

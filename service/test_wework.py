# -*- coding: utf-8 -*-
# @Time    : 2020/12/3 14:49
# @Author  : tongtong
# @File    : test_wework.py
# @Software: Pycharm
import json

import requests

# todo:用例中不能直接出现这种变量定义。需要放到tag类或者更上层的微信类中
corpid = 'wwdb306b2c62dcc0cb'
corpsecret = '44c_m3Su1Z488QCOqHFs5_rihChl-wkTMppHh_p9P5E'


# 该用例中存在的问题
# todo:代码冗余
# todo:与底层框架耦合
# todo:代码封装层次不足，get、post、参数都写在用例中，不利于后续管理


def test_tag_get():
    # 获取access_token的请求
    r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken',
                 params={"corpid": corpid, "corpsecret": corpsecret})
    # 取出token值后续使用
    token = r.json()["access_token"]
    # 获取企业标签库
    r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
        params={'access_token': token},
        json={
            'tag_id': [

            ]
        }
    )
    # 打印返回响应，方便检查错误信息
    # print(r.json())
    # 直接打印，显示格式不好看，转成字符串;indent=2:间隔两个空格---后续可以封装为函数
    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()["errcode"] == 0

    # 添加企业客户标签
    r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
        params={'access_token': token},
        json={
            "group_name": "GROUP_NAME",
            "tag": [
                {
                    "name": "TAG_NAME_1"
                }
            ]
        }

    )
    assert r.status_code == 200
    assert r.json()["errcode"] == 0

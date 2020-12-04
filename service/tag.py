# -*- coding: utf-8 -*-
# @Time    : 2020/12/4 10:30
# @Author  : tongtong
# @File    : tag.py
# @Software: Pycharm
# 封装标签的基本操作
import json

import requests

corpid = 'wwdb306b2c62dcc0cb'
corpsecret = '44c_m3Su1Z488QCOqHFs5_rihChl-wkTMppHh_p9P5E'


class Tag:
    def __init__(self):
        self.token = ""

    # 获取token
    def get_token(self):
        # 获取access_token的请求
        r = requests.get('https://qyapi.weixin.qq.com/cgi-bin/gettoken',
                         params={"corpid": corpid, "corpsecret": corpsecret})
        print(json.dumps(r.json(), indent=2))
        # 取出token值后续使用
        """
        token后边很多接口都需要使用，需要保存在实例里边。此处写成self。token；类里边添加
        def __init__(self):
            self.token = ""
        后续使用方式：self.token
        """
        self.token = r.json()["access_token"]

    # 发起标签组的list
    def list(self):
        r = requests.post("https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            params={'access_token': self.token},
            json={
                'tag_id': []
            }
        )
        print(json.dumps(r.json(), indent=2))
        # 返回r.json()更贴近业务
        # return r.json()
        return r

    # 添加标签。需要传入标签组和标签名称
    def add(self, group_name, tags):
        r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
            params={'access_token': self.token},
            json={
                "group_name": group_name,
                "tag": tags
            }

        )
        print(json.dumps(r.json(), indent=2))
        return r
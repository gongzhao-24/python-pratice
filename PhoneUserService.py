# -*- coding: utf-8 -*-#
import json
import sys
import BaseTemplate
import requests


# Name:
# Description:
# Author:       gongzhao
# Date:         2020/9/27

def encryptPhone(phone):
    url = "http://39.96.183.163:8188/user/queryEncryptedPhone"
    data = {
        "phone": phone
    }
    response = requests.get(url, params=data)
    encryptedPhone = json.loads(response.content).get("data")
    return encryptedPhone


def dencryptPhone(encryptedPhone):
    url = "http://39.96.183.163:8188/user/queryPhone"
    data = {
        "encryptedPhone": encryptedPhone
    }
    response = requests.get(url, params=data)
    phone = json.loads(response.content).get("data")
    return phone


def phone_database(phone):
    return "rds_user" + (int(phone) % 18 / 6)


def phone_table(phone):
    return "AU_PHONE_USER_" + (int(phone) % 18)


def phoneid_database(phoneid):
    return "rds_user" + (int(phoneid) % 36 / 12)


def phoneid_table(phoneid):
    return "AU_PHONE_USER_" + (int(phoneid) % 36)


def unionid_database(unionid):
    return "rds_user" + (get_hash(unionid) % 18 / 6)


def unionid_table(unionid):
    return "AU_PHONE_USER_" + (get_hash(unionid) % 18)


def get_hash(unionid):
    h = 0
    length = len(unionid)
    substring = unionid
    if length > 3:
        substring = unionid[length - 3: length]
    for char in substring:
        h = h + ord(char)
    return h % 18


# 未加密手机号
def get_phone_table_info(phone):
    items = list()
    items.append(BaseTemplate.getitem(encryptPhone(phone), "加密手机号为"))
    items.append(BaseTemplate.getitem(phone_database(phone), "数据库名为"))
    items.append(BaseTemplate.getitem(phone_table(phone), "表名为"))
    jsonBean = {}
    jsonBean['items'] = filter(lambda x: x is not None, items)
    print(json.dumps(jsonBean))
    return json.dumps(jsonBean)


# 加密手机号
def get_encrypted_phone_table_info(encryptedPhone):
    phone = dencryptPhone(encryptedPhone)
    items = list()
    items.append(BaseTemplate.getitem(phone, "解密手机号为"))
    items.append(BaseTemplate.getitem(phone_database(phone), "数据库名为"))
    items.append(BaseTemplate.getitem(phone_table(phone), "表名为"))
    jsonBean = {}
    jsonBean['items'] = filter(lambda x: x is not None, items)
    print(json.dumps(jsonBean))
    return json.dumps(jsonBean)


# 用户id
def get_phoneid_table_info(phoneid):
    items = list()
    items.append(BaseTemplate.getitem(phoneid_database(phoneid), "数据库名为"))
    items.append(BaseTemplate.getitem(phoneid_table(phoneid), "表名为"))
    jsonBean = {}
    jsonBean['items'] = filter(lambda x: x is not None, items)
    print(json.dumps(jsonBean))
    return json.dumps(jsonBean)


# unionid
def get_unionid_table_info(unionid):
    items = list()
    items.append(BaseTemplate.getitem(unionid_database(unionid), "数据库名为"))
    items.append(BaseTemplate.getitem(unionid_table(unionid), "表名为"))

    jsonBean = {}
    jsonBean['items'] = filter(lambda x: x is not None, items)
    print(json.dumps(jsonBean))
    return json.dumps(jsonBean)

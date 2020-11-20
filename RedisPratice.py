# -*- coding: utf-8 -*-#

# Name:         
# Description:
# Author:       gongzhao
# Date:         2020/11/2
import redis as redis

connection = redis.Redis(host="39.105.204.122", port=6379, db=0, password="Huoli@123")
connection.hget
connection.rpush("list", "item1")
connection.rpush("list", "item2")
connection.rpush("list", "item3")
valueList = connection.lrange("list", 0, 20)
print("")

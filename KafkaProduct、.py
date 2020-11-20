#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='124.251.115.187:9092')

msg_dict = {
    "phoneid": "123456",
    "phone": "18664556687",
    "ua": "",
    "timeStamp": "2020-06-10 11:25:10"
}

msg = json.dumps(msg_dict)
producer.send('user_delete_broadcast', bytearray(msg, 'utf-8'), partition=0)
producer.close()

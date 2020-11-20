# -*- coding: utf-8 -*-#

# Name:         
# Description:
# Author:       gongzhao
# Date:         2020/11/10
from BaseReadFile import read_txt_file


def read_file(file_name):
    content = read_txt_file(file_name)
    xxlcount = 0;
    count = 0;
    for index in range(len(content)):
        if "tid" in content[index]:
            count += 1
            print(content[index])
            if "xxl-rpc, NettyHttpServer-serverHandlerPool" in content[index]:
                xxlcount += 1
    print(count)
    print(xxlcount)

def get_url(line):
    list = str(line).split('/')
    return list[2]


read_file("jstack.log")

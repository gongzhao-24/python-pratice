# -*- coding: utf-8 -*-#

# Name:     将公司用户的微信头像和航班管家头像查询出来并存储到excel中
# Description:
# Author:       gongzhao
# Date:         2020/11/3
import json
import urllib

import requests

from BaseReadFile import write_excel_file, read_excel_file
from BaseRequest import normal_request, user_prod_url


def query_corp_user_phoneId():
    url = "http://ssoapi.133.cn/sso-manager-api/user/getUserPhoneId"
    response = requests.post(url)
    phoneidList = json.loads(response.content).get("data")
    return phoneidList


# 根据phoneid 查询用户的头像和微信头像
def query_user_image(phoneid):
    data = {
        "system": "widefield",
        "phoneid": phoneid
    }
    response = normal_request(user_prod_url() + "/user/baseinfo/queryByPhoneidOrPhone", data)
    if response["success"] is False:
        return None
    else:
        user = response['data']['user']
        user_info = {}
        user_info["phoneid"] = phoneid
        if "hbgjImgurl" in user:
            hbgjImgurl = urllib.parse.unquote(user["hbgjImgurl"])
            if "oss.133" in hbgjImgurl:
                user_info["航班管家头像"] = hbgjImgurl
                return user_info
            else:
                return None
        else:
            return None


if __name__ == '__main__':
    row_val_list = ["PHONEID", "HBGJ_HEADIMGURL"]
    content = read_excel_file("image.xls", "Sheet1",row_val_list)
    write_excel_file("image_new.xlsx", row_val_list, content)

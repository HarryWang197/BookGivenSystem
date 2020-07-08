#!/usr/bin/env python3
# @Time    : 2020/3/9 21:40
# @Author  : Harry Wang

# 1.urllib发送请求
# 2.requests
import requests

class HTTP:
    @staticmethod
    def get(url,return_json = True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text #三元表达式
        # if r.status_code == 200:
        #     if return_json:
        #         return r.json()
        #     else:
        #         return r.text
        # else:
        #     if return_json:
        #         return {}
        #     else:
        #         return ''

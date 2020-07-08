#!/usr/bin/env python3
# @Time    : 2020/4/22 15:48
# @Author  : Harry Wang
class TradeInfo:
    def __init__(self, goods):
        self.total = 0
        self.trades = []
        self.__prase(goods)

    def __prase(self, goods):
        self.total = len(goods)
        self.trades = [self.__map_to_trade(single) for single in goods]

    def __map_to_trade(self, single):
        if single.create_datetime:
            time = single.create_datetime.strftime('%Y-%m-%d'),
        else:
            time = '上传时间未知'
        return dict(
            user_name=single.user.nickname,
            time=time,
            id=single.id
        )
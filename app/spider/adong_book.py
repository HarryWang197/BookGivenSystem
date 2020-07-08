#!/usr/bin/env python3
# @Time    : 2020/3/15 20:22
# @Author  : Harry Wang
from flask import current_app

from app.libs.http1 import HTTP


class ADongBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

        # API有访问限制，故每查询一次，就将查询内容放入数据库中，下次查找时就从数据库中查询
    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        result = HTTP.get(url)
        self.__fill_single(result)

    def __fill_collection(self, data):
        if data:
            self.total = data['total']
            self.books = data['books']

    def search_by_keyword(self, keyword, page=1):
        url = self.keyword_url.format(keyword, current_app.config['PER_PAGE'], self.start_method(page))
        result = HTTP.get(url)
        self.__fill_collection(result)

    def start_method(self, page):
        return (page - 1) * current_app.config['PER_PAGE']

    @property
    def first(self):
        return self.books[0] if self.total >= 1 else None

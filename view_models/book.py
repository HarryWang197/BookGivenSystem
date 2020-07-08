#!/usr/bin/env python3
# @Time    : 2020/4/19 15:12
# @Author  : Harry Wang


class BookViewModel:
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.author = '、'.join(book['author'])
        self.price = book['price']
        self.summary = book['summary']
        self.image = book['image']
        self.pages = book['pages']
        self.isbn = book['isbn']
        self.pubdate = book['pubdate']
        self.binding = book['binding']

    @property
    def intro(self):
        intros = filter(lambda x: True if x else False,
                        [self.author, self.publisher, self.price])

        return '/'.join(intros)


class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, adong_book, keyword):
        self.total = adong_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in adong_book.books]

# class BookViewModel:
#     @classmethod
#     # 剪裁单本图书的数据
#     def package_single(cls, data, keyword):
#         returned = {
#             'books': [],
#             'total': 0,
#             'keyword': keyword
#         }
#         if data:
#             returned['total'] = 1
#             returned['books'] = [cls._cut_book_data(data)]
#         return returned
#
#     @classmethod
#     # 剪裁多本图书的数据
#     def package_collection(cls, data, keyword):
#         returned = {
#             'books': [],
#             'total': 0,
#             'keyword': keyword
#         }
#         if data:
#             returned['total'] = data['total']
#             returned['books'] = [cls._cut_book_data(book) for book in data['books']]
#         return returned
#
#     @classmethod
#     def _cut_book_data(cls, data):
#         book = {
#             'title': data['title'],
#             'publisher': data['publisher'],
#             'pages': data['pages'] or '',
#             'author': '、'.join(data['author']),
#             # 原数据中author内是列表，需要遍历才能得到
#             'price': data['price'],
#             'summary': data['summary'] or '',
#             'image': data['image']
#         }
#         return book

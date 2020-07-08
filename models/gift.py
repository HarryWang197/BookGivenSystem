#!/usr/bin/env python3
# @Time    : 2020/4/21 11:59
# @Author  : Harry Wang
from flask import current_app
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, desc, func
from sqlalchemy.orm import relationship

from app.spider.adong_book import ADongBook
from models.base import db, Base


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)
    isbn = Column(String(13), nullable=False)
    launched = Column(Boolean, default=False)

    def is_yourself_gift(self, uid):
        return True if self.uid == uid else False

    @classmethod
    def get_wish_counts(cls, isbn_list):
        from models.wish import Wish
        # 根据传入的isbn_list,到wish表中计算出某个礼物的wish心愿数量
        # mysql in
        count_list = db.session.query(func.count(Wish.id), Wish.isbn).filter(Wish.launched == False,
                                  Wish.isbn.in_(isbn_list),
                                  Wish.status == 1).group_by(Wish.isbn).all()
        count_list = [{'count':w[0], 'isbn':w[1]} for w in count_list]
        return count_list

    @classmethod
    def get_user_gift(cls, uid):
        gifts = Gift.query.filter_by(uid=uid, launched=False).order_by(
            desc(Gift.create_time)).all()
        return gifts

    @property
    def book(self):
        adong_book = ADongBook()
        adong_book.search_by_isbn(self.isbn)
        return adong_book.first
    # 限定显示数量RECENT_BOOK_COUNT=30
    # 按上传时间排序order_by
    # 去重（group_by）
    # 对象代表一个礼物
    # 类代表礼物这个事物，是抽象的一类礼物，而不是具体的一个
    @classmethod
    def recent(cls):
        # 链式调用
        recent_gift = Gift.query.filter_by(
            launched=False).group_by(
            Gift.isbn).order_by(
            desc(Gift.create_time)).limit(
            current_app.config['RECENT_BOOK_COUNT']).all()
        return recent_gift


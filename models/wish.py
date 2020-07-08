#!/usr/bin/env python3
# @Time    : 2020/4/21 11:59
# @Author  : Harry Wang
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, desc, func
from sqlalchemy.orm import relationship

from app.spider.adong_book import ADongBook
from models.base import Base, db


class Wish(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)
    isbn = Column(String(13), nullable=False)
    launched = Column(Boolean, default=False)

    @classmethod
    def get_gifts_counts(cls, isbn_list):
        from models.gift import Gift
        # 根据传入的isbn_list,到wish表中计算出某个礼物的wish心愿数量
        # mysql in
        count_list = db.session.query(func.count(Gift.id), Gift.isbn).filter(Gift.launched == False,
                                                                             Gift.isbn.in_(isbn_list),
                                                                             Gift.status == 1).group_by(
            Gift.isbn).all()
        count_list = [{'count': w[0], 'isbn': w[1]} for w in count_list]
        return count_list

    @classmethod
    def get_user_wishes(cls, uid):
        wishes = Wish.query.filter_by(uid=uid, launched=False).order_by(
            desc(Wish.create_time)).all()
        return wishes

    @property
    def book(self):
        adong_book = ADongBook()
        adong_book.search_by_isbn(self.isbn)
        return adong_book.first
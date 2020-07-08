#!/usr/bin/env python3
# @Time    : 2020/3/21 21:23
# @Author  : Harry Wang

from sqlalchemy import Column, Integer, String
from models.base import db


class Book(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    # Column类中需要输入键值类型等信息，autoincrement为自增长
    title = Column(String(50), nullable=False)
    # nullable为是否为空
    _author = Column('author', String(30), default='佚名')
    binding = Column(String(20))
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    isbn = Column(String(15), nullable=False, unique=True)
    summary = Column(String(1000))
    image = Column(String(50))

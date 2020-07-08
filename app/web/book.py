#!/usr/bin/env python3
# @Time    : 2020/3/15 21:11
# @Author  : Harry Wang

from flask import jsonify, request, render_template, flash
from flask_login import current_user

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.adong_book import ADongBook
from models.gift import Gift
from models.wish import Wish
from view_models.book import BookViewModel, BookCollection
from view_models.trade import TradeInfo
from . import web


# 实例化蓝图对象
@web.route('/book/search')
def search():
    """
    :param q: 关键字或ISBN
    :param page: 
    ?q=isbn&page=1
    """

    # 用Request传递参数，因为url不能写成book/serach?q=__&page=_
    # 若想上述这样根据参数访问url只能用Request类
    # q = request.args['q']
    # 条件限制（至少一个字符，长度限制）
    # page = request.args['page']
    # 正整数，最大值限制
    # Flask用插件进行校验————wtforms

    # 验证层

    form = SearchForm(request.args)  # 调用SearchForm进行校验
    q = form.q.data.strip()  # 获得参数且strip用于去空格
    page = form.page.data
    books = BookCollection()

    if form.validate():
        # 必须要用validate方法初始化，否则报错
        isbn_or_key = is_isbn_or_key(q)
        adong_book = ADongBook()

        if isbn_or_key == 'isbn':
            adong_book.search_by_isbn(q)
            # result = ADongBook.search_by_isbn(q)
            # result = BookViewModel.package_single(result, q)
        else:
            adong_book.search_by_keyword(q, page)
            # result = ADongBook.search_by_keyword(q, page)
            # result = BookViewModel.package_collection(result, q)

        # python不能直接取序列化对象
        # __dict__将会把每个对象里的数据通过字典返回
        books.fill(adong_book, q)

        # default需要返回可以序列化的函数，也就是该对象内部的对象，用lambda表达式来定义该函数
        # return jsonify(result)
    else:
        flash('搜索的关键字不符合要求，请重新输入关键字')
        # return jsonify(form.errors)
    return render_template('search_result.html', books=books, form=form)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    has_in_wishes = False
    has_in_gifts = False

    # 取书籍详情数据
    adong_book = ADongBook()
    adong_book.search_by_isbn(isbn)
    book = BookViewModel(adong_book.first)

    if current_user.is_authenticated:
        if Gift.query.filter_by(uid=current_user.id,
                             isbn=isbn, launched=False).first():
            has_in_gifts = True
        if Wish.query.filter_by(uid=current_user.id,
                             isbn=isbn, launched=False).first():
            has_in_wishes = True

    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

    trade_wishes_models = TradeInfo(trade_wishes)
    trade_gifts_models = TradeInfo(trade_gifts)

    return render_template('book_detail.html', book=book,
                           wishes=trade_wishes_models, gifts=trade_gifts_models,
                           has_in_wishes=has_in_wishes, has_in_gifts=has_in_gifts)


@web.route('/test')
def test():
    r = {
        'name': '王维东',
        'age': 19
    }
    r1 = {
        'name': '王维东',
        'age': 18
    }
    return render_template('test.html', data=r, data1=r1)
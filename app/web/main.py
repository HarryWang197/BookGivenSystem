from flask import render_template
from flask_login import login_required, current_user

from models.gift import Gift
from view_models.book import BookViewModel
from . import web


__author__ = '王维东'


@web.route('/')
def index():
    recent_gift = Gift.recent()
    books = [BookViewModel(gift.book) for gift in recent_gift]
    return render_template('index.html', recent=books)


@web.route('/personal')
@login_required
def personal_center():
    return render_template('personal.html', user=current_user.summary)
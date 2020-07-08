#!/usr/bin/env python3
# @Time    : 2020/3/16 16:40
# @Author  : Harry Wang
from flask import Flask
from models.book import db
from flask_login import LoginManager
from flask_mail import Mail
from models.user import User

login_manager = LoginManager()
mail = Mail()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)
    # 调用注册好的蓝图对象

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或注册'
    # 关联db插件与app核心对象
    mail.init_app(app)

    # @login_manager.user_loader
    # def load_user(user_id):
    #     user = db.session.query(User).get(int(user_id))
    #     return user

    @login_manager.user_loader
    def get_user(uid):
        return User.query.get(int(uid))

    with app.app_context():
        db.create_all()
    return app


def register_blueprint(app):
    # 注册蓝图
    from app.web.book import web
    app.register_blueprint(web)
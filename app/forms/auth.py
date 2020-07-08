#!/usr/bin/env python3
# @Time    : 2020/4/21 12:33
# @Author  : Harry Wang
from flask import flash
from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, ValidationError, EqualTo

from models.user import User


class RegisterForm(Form):
    email = StringField(validators=[DataRequired('电子邮箱不能为空，请输入你的邮箱'), Length(8, 64),
                                    Email(message='电子邮箱格式不符合规范')])

    nickname = StringField('昵称', validators=[
        DataRequired('昵称不能为空，请输入你的昵称'), Length(2, 10, message='昵称至少需要2个字符，最多10个字符')])

    password = PasswordField('密码', validators=[
        DataRequired('密码不能为空，请输入你的密码'), Length(6, 20, message='密码至少需要6个字符，最多32个字符')])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('该邮箱已被注册')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('该昵称已存在')


class LoginForm(Form):
    email = StringField(validators=[DataRequired('电子邮箱不能为空，请输入你的邮箱'), Length(8, 64),
                                    Email(message='电子邮箱不符合规范')])

    password = PasswordField('密码', validators=[
        DataRequired(message='密码不可以为空，请输入你的密码'), Length(6, 32)])


class EmailForm(Form):
    email = StringField(validators=[DataRequired('电子邮箱不能为空，请输入你的邮箱'), Length(8, 64),
                                    Email(message='电子邮箱格式不符合规范')])


class ChangePasswordForm(Form):
    old_password = PasswordField('原有密码', validators=[DataRequired('密码不可以为空，请输入你的密码')])
    new_password1 = PasswordField('新密码', validators=[
        DataRequired('密码不可以为空，请输入你的密码'), Length(6, 32, message='密码长度至少需要在6到32个字符之间'),
        EqualTo('new_password2', message='两次输入的密码不一致')])
    new_password2 = PasswordField('确认新密码字段', validators=[DataRequired('密码不可以为空，请输入你的密码')])


class ResetPasswordForm(Form):
    password1 = PasswordField('新密码', validators=[
        DataRequired('密码不能为空，请输入你的密码'), Length(6, 32, message='密码长度至少需要在6到32个字符之间'),
        EqualTo('password2', message='两次输入的密码不相同')])
    password2 = PasswordField('确认新密码', validators=[
        DataRequired('密码不能为空，请输入你的密码'), Length(6, 32)])


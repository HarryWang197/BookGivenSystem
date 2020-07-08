#!/usr/bin/env python3
# @Time    : 2020/3/17 13:03
# @Author  : Harry Wang
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired, Regexp


class SearchForm(Form):
    q = StringField(validators=[Length(min=1, max=30, message='不能小于1个字符，也不能大于30个字符')])
    # DataRequired用于防止空格输入但能搜索成功的情况，search?q= &page=1
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)


class DriftForm(Form):
    recipient_name = StringField(
        '收件人姓名', validators=[DataRequired("收件人不能为空"), Length(min=2, max=20,
                                                    message='收件人姓名长度必须在2到20个字符之间')])
    mobile = StringField('手机号', validators=[DataRequired("手机号不能为空"),
                                            Regexp('^1[0-9]{10}$', 0, '请输入正确的手机号')])
    message = StringField('留言',validators=[DataRequired("说点什么吧！")])
    address = StringField(
        '邮寄地址', validators=[DataRequired("邮寄地址不能为空"),
                            Length(min=10, max=70, message='地址还不到10个字吗？尽量写详细一些吧')])

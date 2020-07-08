#!/usr/bin/env python3
# @Time    : 2020/3/16 12:05
# @Author  : Harry Wang

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')


@app.route('/hello')
def hello():
    return 'how are you'

if __name__ == '__main__':
    app.run(debug = app.config['DEBUG'])
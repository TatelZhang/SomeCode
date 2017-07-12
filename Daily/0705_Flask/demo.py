#! /usr/bin/env python
# coding = utf-8

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/some')
def some():
    return render_template('some.html')


if __name__ == '__main__':
    app.run(debug=True)

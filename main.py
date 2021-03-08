from collections import namedtuple
from sender import send
from flask import Flask, render_template, redirect, url_for
from flask import request as r

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')


@app.route('/request', methods=['POST'])
def request():
    url = r.form['url']
    amount = r.form['amount']
    coupon = r.form['coupon']
    send(url, amount, coupon)
    return redirect(url_for('main'))
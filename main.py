from collections import namedtuple
from sender import send
from flask import Flask, render_template, redirect, url_for
from flask import request as r
import os

app = Flask(__name__)

Message = namedtuple('Message', 'text tag')
messages = []


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

if __name__ == "__main__":
    from waitress import serve
    ip = os.system('hostname -I')
    print(ip)
    serve(app, host=str(ip), port=5000)
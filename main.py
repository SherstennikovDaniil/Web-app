from collections import namedtuple

from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def Hello():
    return render_template('index.html')


@app.route('/main')
def main():
    return render_template('main.html')

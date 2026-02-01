from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/5а.html')
def fifth_a():
    return render_template('5а.html')
@app.route('/5б.html')
def fifth_b():
    return render_template('5б.html')
@app.route('/5в.html')
def fifth_v():
    return render_template('5в.html')
@app.route('/6а.html')
def sixth_a():
    return render_template('6а.html')
@app.route('/6б.html')
def sixth_b():
    return render_template('6б.html')
@app.route('/6в.html')
def sixth_v():
    return render_template('6в.html')
@app.route('/7а.html')
def seventh_а():
    return render_template('7а.html')
@app.route('/7б.html')
def seventh_b():
    return render_template('7б.html')
@app.route('/8а.html')
def eighth_а():
    return render_template('8а.html')
@app.route('/8б.html')
def eighth_b():
    return render_template('8б.html')
@app.route('/9а.html')
def ninth_а():
    return render_template('9а.html')
@app.route('/10а.html')
def tenth_а():
    return render_template('10а.html')
@app.route('/11а.html')
def eleventh_а():
    return render_template('11а.html')
@app.route('/index.html')
def returned():
    return render_template('index.html')
@app.route('/yandex_0c1a34acd4468fc7.html')
def check():
    return render_template('yandex_0c1a34acd4468fc7.html')


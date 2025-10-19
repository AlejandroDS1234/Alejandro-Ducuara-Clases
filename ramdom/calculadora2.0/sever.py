from flask import Flask, render_template

cal=Flask(__name__)

@cal.route('/')
def index():
    return render_template("index.html")

@cal.route('/calculadora')
def calculadora():
    return render_template('calculadora.html')

@cal.route('/calculadora1')
def calculadora1():
    return render_template('calculadora1.html')


if __name__=="__main__":
    cal.run(debug=True)
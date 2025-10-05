from flask import Flask, render_template

cal=Flask(__name__)

@cal.route('/')
def index():
    return render_template("index.html")

if __name__=="__main__":
    cal.run(debug=True)
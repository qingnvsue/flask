from flask import Flask, render_template
app = Flask(__name__)

class DataStore():
    a = None
    c = None

data = DataStore()

@app.route("/index")
def index():
    a=3
    b=4
    c=a+b
    data.a=a
    data.c=c
    return render_template("index.html",c=c)

@app.route("/dif")
def dif():
    d=data.c+data.a
    return render_template("dif.html",d=d)

if __name__ == "__main__":
    app.run(debug=True)
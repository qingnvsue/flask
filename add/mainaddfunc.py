from flask import Flask, render_template, request
from add import *
from divide import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('button.html')

@app.route('/add', methods=['GET'])
def add():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add1():
        a = request.form['adder1']
        b = request.form['adder2']
        try:
            a = float(a)
            b = float(b)
            result = sum_function(a, b)
            return render_template('index.html', result=result, var1=a, var2=b)
        except:
            return render_template('index.html', message='inputs false!!!', var1=a, var2=b)


@app.route('/divide', methods=['GET'])
def divide():
    return render_template('index1.html')

@app.route('/divide', methods=['POST'])
def divide1():
        a = request.form['adder1']
        b = request.form['adder2']
        try:
            a = float(a)
            b = float(b)
            result = divide_function(a, b)
            return render_template('index1.html', result=result, var1=a, var2=b)
        except:
            return render_template('index1.html', message='inputs false!!!', var1=a, var2=b)
        
if __name__ == '__main__':
        app.debug = True
        app.run(port=8001)

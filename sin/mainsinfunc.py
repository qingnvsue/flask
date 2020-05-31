from flask import Flask, render_template, request, url_for
from sin import *
import matplotlib.pyplot as plt
import io
import base64
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index4.html')

@app.route('/', methods=['POST'])
def add():
        A = request.form['attitude']
        f = request.form['frequency']
        xmin = request.form['xmin']
        xmax = request.form['xmax']
        try:

            A = float(A)
            f = float(f)
            xmin = float(xmin)
            xmax = float(xmax)
            x, y = sin_function(A, f, xmin, xmax)

            img = io.BytesIO()
            plt.plot(x, y)
            plt.rcParams['font.sans-serif'] = ['SimHei']
            plt.rcParams['axes.unicode_minus'] = False
            plt.title('正弦函数')
            plt.xlabel('x')
            plt.ylabel('y')
            plt.savefig(img, format='png')
            img.seek(0)

            plot_url = base64.b64encode(img.getvalue()).decode()
            return render_template('index1.html', var1=A, var2=f, var3=xmin, var4=xmax, plot_url=plot_url)
        except:
            return render_template('index4.html', message='inputs false!!!', var1=A, var2=f, var3=xmin, var4=xmax)
        
if __name__ == '__main__':
    app.run(port=8002)
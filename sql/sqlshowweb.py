from flask import Flask
from flask import render_template
import pymysql

app = Flask(__name__)


@app.route('/')
def index():
    conn = pymysql.connect(host='39.106.168.84', user='xxxx', password='xxxxxxxx', port=3306,
                        db='flask_topvj_net')
    cur = conn.cursor()
    sql = "SELECT `name`, `age` FROM `student` WHERE 1"
    cur.execute(sql)
    u = cur.fetchall()
    conn.close()
    return render_template('index.html',u=u)
if __name__ == '__main__':
    app.debug = True
    app.run(port=8003)
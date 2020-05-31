from flask import Flask, render_template, request
import pymysql
app = Flask(__name__)

class DataStore():
    a = None
data = DataStore()

@app.route('/', methods=['GET'])
def home():
    return render_template('index2.html')


@app.route('/', methods=['POST'])
def add():
    id = request.form['id']
    data.a = id
    name = request.form['name']
    age = request.form['age']
    sex= request.form['sex']
    try:
        id= float(id)
        age = float(age)
        conn = pymysql.connect(host='39.106.168.84', user='flask_topvj_net', password='xxxxxx', port=3306,
                               db='flask_topvj_net')
        cur = conn.cursor()  # 生成游标对象
        sql = "INSERT INTO `student`(`id`, `name`, `age`, `sex`) VALUES (%s,%s,%s,%s)",(id, name, age, sex)
        try:
            # 执行sql语句
            cur.execute(*sql)
            # 提交到数据库执行
            conn.commit()
        except:
            # 如果发生错误则回滚
            conn.rollback()

        sql = "SELECT * FROM `student` WHERE `id` = %s" % data.a
        cur.execute(sql)
        u = cur.fetchall()
        conn.close()
        return render_template('index3.html', u=u)
        conn.close()
    except:
        return render_template('index2.html', message='inputs false!!!', var1=id, var2=name, var3=age, var4=sex)


if __name__ == '__main__':
    app.run(port=8002)
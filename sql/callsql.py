import pymysql
#连接数据库
conn = pymysql.connect(host='39.106.168.84', user='flask_topvj_net', password='ZmBfzGjYnH87wJPR', port=3306, db='flask_topvj_net')

cur = conn.cursor() # 生成游标对象
sql="select * from `student` " # SQL语句
cur.execute(sql) # 执行SQL语句
data = cur.fetchall() # 通过fetchall方法获得数据
for i in data[:2]: # 打印输出前2条数据
   print (i)
cur.close() # 关闭游标
conn.close() # 关闭连接

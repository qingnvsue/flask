import pymysql
#连接数据库
conn = pymysql.connect(host='39.106.168.84', user='flask_topvj_net', password='xxxxx', port=3306, db='flask_topvj_net')

cur = conn.cursor() # 生成游标对象

'''
sql="select * from `student` " # SQL语句
cur.execute(sql) # 执行SQL语句
data = cur.fetchall() # 通过fetchall方法获得数据
for i in data[:2]: # 打印输出前2条数据
   print (i)
cur.close() # 关闭游标
conn.close() # 关闭连接
'''
'''
# 使用 execute() 方法执行 SQL，如果表存在则删除
cur.execute("DROP TABLE IF EXISTS EMPLOYEE")
# 使用预处理语句创建表
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
cur.execute(sql)
# 关闭数据库连接
conn.close()
'''

'''
# SQL 插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
   # 执行sql语句
   cur.execute(sql)
   # 提交到数据库执行
   conn.commit()
except:
   # 如果发生错误则回滚
   conn.rollback()

# 关闭数据库连接
conn.close()
'''

'''
# SQL 查询语句
sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > %s" % (1000)
try:
   # 执行SQL语句
   cur.execute(sql)
   # 获取所有记录列表
   results = cur.fetchall()
   for row in results:
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      # 打印结果
      print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
            (fname, lname, age, sex, income))
except:
   print("Error: unable to fetch data")

# 关闭数据库连接
conn.close()
'''

'''
# SQL 更新语句
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
try:
   # 执行SQL语句
   cur.execute(sql)
   # 提交到数据库执行
   conn.commit()
except:
   # 发生错误时回滚
   conn.rollback()

# 关闭数据库连接
conn.close()
'''

a=5
b='lili'
c=25
d='f'
# SQL 插入语句
sql = "INSERT INTO `student`(`id`, `name`, `age`, `sex`) VALUES (%s,%s,%s,%s)",(a,b,c,d)
try:
   # 执行sql语句
   cur.execute(*sql)
   # 提交到数据库执行
   conn.commit()
except:
   # 如果发生错误则回滚
   conn.rollback()

# 关闭数据库连接
conn.close()


'''
# SQL 查询语句
sql = "SELECT `id`, `age` FROM `student` WHERE 1"

   # 执行SQL语句
try:
   cur.execute(sql)
   # 获取所有记录列表
   results = cur.fetchall()
   for row in results:
      id = row[0]
      age = row[1]
      age=age+1
      # 打印结果
      print("id=%s,age=%s" % \
            (id, age,))
except:
   print("Error: unable to fetch data")

# 关闭数据库连接
conn.close()
'''

'''
# SQL 查询语句
sql = "SELECT `id`, `age` FROM `student` WHERE `age` = 20"

   # 执行SQL语句
try:
   cur.execute(sql)
   # 获取所有记录列表
   results = cur.fetchall()
   for row in results:
      id = row[0]
      age = row[1]
      age=age+1
      # 打印结果
      print("id=%s,age=%s" % \
            (id, age,))
except:
   print("Error: unable to fetch data")

# 关闭数据库连接
conn.close()
'''
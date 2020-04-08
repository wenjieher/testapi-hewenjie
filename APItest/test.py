# 导入pymysql模块
import pymysql
# 连接database
conn = pymysql.connect(host="192.168.230.19", user="admin",password="Db2019@#Wdit",database="wdit-activity",charset="utf8")
# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor()
# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")
# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)
#执行查询语句
cursor.execute('select * from wx_act_signgift_registration')
#读取表里所有的数据
for i in range(cursor.rowcount):
    row=cursor.fetchone()
    if row[3] == '18817503313':
        print('pass')
        print(row[3])


# 关闭数据库连接
conn.close()
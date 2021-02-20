# 一、python连接数据库
# 1、链接数据库
import pymysql as pysql
conn = pysql.connect(
    host='localhost',
    user='root',
    passwd='P@ssw0rd',
    db='JsshiDataBase',
    charset='utf8'
)
# python，必须有一个游标对象，用来给数据库发送sql语句，并执行。
# 2、创建游标对象
curl = conn.cursor()
# 3、对数据库进行增删改查操作。
# 1)**************创建数据表**************
try:
    create_sqli = "create table helloMySQL (id int, name varchar(255));"
    curl.execute(create_sqli)
except Exception as e:
    print("数据表创建失败", e)
else:
    print("数据表创建成功;")
# 2)**************插入数据**************
try:
    insert_sqli = "insert into helloMySQL values(2, 'Jsshi');"
    curl.execute(insert_sqli)
except Exception as e:
    print("插入数据失败！", e)
else:
    # 如果是插入数据， 一定要提交数据， 不然数据库中找不到要插入的数据;
    conn.commit()
    print("插入数据成功;")
# 3)**************插入多条数据**************
try:
    info = [(i, "westos%s" %(i)) for i in range(100)]
    # *********************第一种方式********************
    # %s必须手动添加一个字符串， 否则就是一个变量名， 会报错.
    # insert_sqli = "insert into helloMySQL values(%d, '%s');"
    # for item in info:
    #    print("insert 语句", insert_sqli %item)
    #    curl.execute(insert_sqli %item)
    # *********************第二种方式********************
    # insert_sqli = "insert into helloMySQL values(%s, %s)"
    # curl.executemany(insert_sqli, info)
except Exception as e:
    print("插入多条数据失败:", e)
else:
    # 如果是插入数据,一定要提交数据,不然数据库中找不到要插入的数据;
    conn.commit()
    print("插入多条数据成功;")
# 4)**************************数据库查询*****************************
sqli = "select * from helloMySQL;"
result = curl.execute(sqli)  # 默认不返回查询结果集,返回数据记录数。
print(result)
# print(curl.fetchone())  # 1). 获取下一个查询结果集;
# print(curl.fetchone())
# print(curl.fetchone())
# print(curl.fetchone())
# print(curl.fetchone())
# print(curl.fetchmany(4))  # 2). 获取制定个数个查询结果集；
info = curl.fetchall()  # 3). 获取所有的查询结果
print(info)
print(len(info))
print(curl.rowcount)
# 5)移动游标指针
print(curl.fetchmany(3))
print("正在移动指针到最开始。。。。")
curl.scroll(0, "absolute")
print(curl.fetchmany(3))
print("正在移动指针到倒数第2个。。。")
print(curl.fetchall())  # 移动到最后
curl.scroll(-2, mode="relative")
print(curl.fetchall())
curl.close()  # 关闭游标
conn.close()  # 关闭链接

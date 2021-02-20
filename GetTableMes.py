# 二、获取表的字段名和信息
import pymysql as pysql
import time as time
import numpy
from flask import Flask, jsonify, request
conn = pysql.connect(
    host="localhost",
    user="root",
    passwd="P@ssw0rd",
    db="JsshiDataBase",
    charset="utf8"
)
# 创建游标
curl = conn.cursor()
# 游标调用sql
sqli = "select * from helloMySQL;"
# 通过游标执行sql
curl.execute(sqli)
# 获取标中所有的数据，转存对象
data = curl.fetchall()
curl.close()
conn.close()
jsonData = []
for i in data:
    result = {"id": (i[0],), "name": i[1]}
    jsonData.append(result)
    print(result)
app = Flask(__name__)  # 创建一个服务
@app.route('/get_userData', methods=['post'])
def get_userData():
    return jsonify(jsonData)
app.run(host="0.0.0.0", port=8802, debug=False)
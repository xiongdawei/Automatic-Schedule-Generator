import execjs

<!DOCTYPE html>
<html>
<head>
<script>
function myFunction()
{
    alert("你好，我是一个警告框！");
}
</script>
</head>
<body>

<input type="button" onclick="myFunction()" value="显示警告框">

</body>
</html>

from flask import Flask,session
import os
from datetime import timedelta
 4 app = Flask(__name__)
 5 app.config['SECRET_KEY']=os.urandom(24)   #设置为24位的字符,每次运行服务器都是不同的，所以服务器启动一次上次的session就清除。
 6 app.config['PERMANENT_SESSION_LIFETIME']=timedelta(days=7) #设置session的保存时间。
 7 #添加数据到session
 8 #操作的时候更操作字典是一样的
 9 #secret_key:----------盐，为了混淆加密。
10 
11 
12 @app.route('/')
13 def hello_world():
14     session.permanent=True  #默认session的时间持续31天
15     session['username'] = 'xxx'
16 
17     return 'Hello World!'
18 
19 #获取session
20 @app.route('/get/')
21 def get():
22     return  session.get('username')
23 
24 #删除session
25 @app.route('/delete/')
26 def delete():
27     print(session.get('username'))
28     session.pop('username')
29     print(session.get('username'))
30     return 'delete'
31 #清楚session
32 @app.route('/clear/')
33 def clear():
34     print(session.get('username'))
35     session.clear()
36     print(session.get('username'))
37     return 'clear'
38 
39 if __name__ == '__main__':
40     app.run(debug=True)


 
# 设置cookie
@app.route("/set_cookie")
def set_cookie():
    resp = make_response("success")  # "success"是响应体
    # 设置cookie, 默认有效期是临时cookie，浏览器关闭就失效
    resp.set_cookie("Name", "Python")
    # max_age设置有效期，单位：秒
    resp.set_cookie("Name2", "Python1", max_age=3600)
    # 设置cookie其实就是通过设置响应头实现的。
    # resp.headers["Set-Cookie"] = "Name3=Python3; Expires=Sat, 18-Nov-2017 04:36:04 GMT; Max-Age=3600; Path=/"
    return resp
 
 
# 获取cookie
@app.route("/get_cookie")
def get_cookie():
    c = request.cookies.get("Name")
    return c
 
 
# 删除cookie
@app.route("/delete_cookie")
def delete_cookie():
    resp = make_response("del success")
    # 删除cookie
    resp.delete_cookie("Name1")
    return resp
 
 
if __name__ == '__main__':

import pdfkit

# 有下面3中途径生产pdf

pdfkit.from_url('http://google.com', 'out.pdf')

pdfkit.from_file('test.html', 'out.pdf')

pdfkit.from_string('Hello!', 'out.pdf')
--------------------- 
作者：振裕 
来源：CSDN 
原文：https://blog.csdn.net/suzyu12345/article/details/50759482 
版权声明：本文为博主原创文章，转载请附上博文链接！






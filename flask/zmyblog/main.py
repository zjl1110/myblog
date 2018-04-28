# -*-coding:utf-8 -*-  
__author__ = "ZJL"

from flask import Flask
from flask import request,send_from_directory,url_for,session
import json
import base64
import os
from werkzeug.utils import secure_filename
from flask_cors import CORS
import socket
from common.getuserdata import getuserdata,getcontent,getcontentcount,getcontenttype,logindatadb,editmycontent,\
    setlogintoken,delmycontent,usertoken,setheadimg,setmyintroduction,setmypassword,addmytype,setmytype,delmytype
import time

# 自腾讯云上下面获取ip的代码返回的是127.0.0.1，请填写自己服务器ip
hostip = socket.gethostbyname(socket.gethostname())

app = Flask(__name__)
CORS(app, supports_credentials=True)

# app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

#测试页面
@app.route('/')
def hello_world():
    return 'Hello World!'

#图片格式
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

#图片存储目录
app.config['UPLOAD_FOLDER'] = os.getcwd()+os.sep+"img"

#上传文件大小限制
app.config['MAX_CONTENT_LENGTH'] = 6 * 1024 * 1024

#判断图片格式是否正确
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

#获取图片
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

#上传图片
@app.route('/imgupdata', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST' and request.form.get('username') and request.form.get('token'):
        file = request.files['file']
        contentdata = request.form.to_dict()
        username = contentdata.get("username","")
        token = contentdata.get("token", "")
        userid = contentdata.get("userid", "")
        headimg = contentdata.get("headimg", "")
        kwargs = {"username": username, "token": token}
        data = imgupdata(file,userid,headimg,**kwargs)
        return json.dumps(data)
    return ""

#图片上传的token验证
@usertoken
def imgupdata(file,userid,headimg,**kwargs):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filename = filename.split(".")[0] + str(int(time.time())) + "." + filename.split(".")[-1]
        print(filename, "==========")
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        file_url = url_for('uploaded_file', filename=filename)
        imgurl = "http://" + hostip + ":5000" + file_url
        print("imgurl",imgurl)
        urldata = {"imgurl":imgurl}
        if userid and headimg=="1":
            data = setheadimg(userid,imgurl)
            if data:
                return urldata
            else:
                return {"code":"头像修改错误"}
        return urldata

#个人简介
@app.route("/introduction", methods=['GET'])
def introduction_py():
    if request.method == 'GET' :
        jjdata = getuserdata()
        return json.dumps(jjdata)
    else:
        return json.dumps({
            "error":"简介请求错误"
        })

#pdf简历
@app.route("/jlpdf", methods=['GET'])
def get_pdf():
    filename = "zjljl.pdf"
    if request.method == 'GET':
        UPLOAD_FOLDER_PDF = os.getcwd()
        for root, dirs, files in os.walk(UPLOAD_FOLDER_PDF):
            for file in files:
                if file.rsplit('.', 1)[1] == "pdf":
                    filename = file
        with open(filename,"rb") as openpdf:
            base64_data = base64.b64encode(openpdf.read())
            pdfdata = {
                "pdfdata": "data:application/pdf;base64,"+base64_data.decode('utf-8')
            }
            return json.dumps(pdfdata)
    else:
        return json.dumps({
            "error": "pdf请求错误"
        })

#上传pdf
@app.route('/pdfupdata', methods=['GET', 'POST'])
def upload_pdf():
    if request.method == 'POST' and request.form.get('username') and request.form.get('token'):
        file = request.files['file']
        contentdata = request.form.to_dict()
        username = contentdata.get("username", "")
        token = contentdata.get("token", "")
        kwargs = {"username": username, "token": token}
        data = uppdf(file,**kwargs)
        return json.dumps(data)

#上传pdf的token验证
@usertoken
def uppdf(file,**kwargs):
    # pdf格式
    ALLOWED_EXTENSIONS_PDF = set(['pdf'])
    # pdf存储目录
    UPLOAD_FOLDER_PDF = os.getcwd()
    filename = file.filename
    # 判断格式是否正确
    if file and ('.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS_PDF):
        # filename = secure_filename(filename)
        file.save(os.path.join(UPLOAD_FOLDER_PDF, "zjljl.pdf"))
        return {"code": "0"}
    else:
        return {"code": "上传失败"}


#分类
@app.route("/getmenulist",methods=['GET'])
def get_menulist():
    if request.method == 'GET':
        contenttype = getcontenttype()
        return json.dumps({"typedatas":contenttype})
    else:
        return json.dumps({"code":"分类请求错误"})

#内容
@app.route("/getcontentlist",methods=['GET'])
def get_contents():
    print(request.args.get("display"),request.args.get("contenttype"),request.args.get("current"))
    if request.method == 'GET' and request.args.get("display") and request.args.get("current") and request.args.get("contenttype"):
        getdatas = request.args.to_dict()
        display = getdatas.get("display","")
        current = getdatas.get("current","")
        contenttype = getdatas.get("contenttype","")
        datalength = getcontentcount(contenttype)
        new_datas = getcontent(contenttype,current,display)
        jsondata = {
            "total": datalength,
            "display": display,
            "current": current,
            "datas": new_datas
        }
        return json.dumps(jsondata)
    else:
        return json.dumps({
            "error": "分页请求错误"
        })

# 登入
@app.route("/login",methods=['POST'])
def login_py():
    if request.method == 'POST' and request.form.get('username') and request.form.get('password'):
        logindata = request.form.to_dict()
        username = logindata.get('username', "")
        password = logindata.get('password', "")
        print(username,password)
        data = logindatadb(username,password)
        print("cccc",data)
        if data:
            usertoken = setlogintoken(username)
            print("seesion",usertoken)
            return json.dumps({"code":"0","token":usertoken,"username":username})
        else:
            return json.dumps({"code": "用户名密码错误"})
    else:
        return json.dumps({"error": "登入请求失败"})


#编写文章
@app.route("/editcontent",methods=['POST'])
def editcontent():
    if request.method == 'POST' and request.form.get('type') and request.form.get('content') and request.form.get('title') and request.form.get('username') and request.form.get('token'):
        contentdata = request.form.to_dict()
        ctype = contentdata.get('type', "")
        content = contentdata.get('content', "")
        title = contentdata.get('title', "")
        username = contentdata.get('username', "")
        token = contentdata.get('token', "")
        conid = contentdata.get("conid", "")
        print("contentid", conid)
        kwargs = {"username":username,"token":token}
        data = editmycontent(conid,ctype,content,title,**kwargs)
        return json.dumps(data)
    else:
        return json.dumps({"code":"编辑文章请求失败"})

#删除文章
@app.route("/delcontent",methods=['POST'])
def delcontent():
    if request.method == 'POST' and request.form.get('conid') and request.form.get('username') and request.form.get('token'):
        contentdata = request.form.to_dict()
        username = contentdata.get('username', "")
        token = contentdata.get('token', "")
        conid = contentdata.get("conid", "")
        kwargs = {"username": username, "token": token}
        print(kwargs)
        data = delmycontent(conid,**kwargs)
        return json.dumps(data)
    else:
        return json.dumps({"code": "删除文章请求失败"})

# 修改简介
@app.route("/setintroduction",methods=['POST'])
def setintroduction():
    if request.method == 'POST' and request.form.get('userid') and request.form.get('content') and request.form.get('username') and request.form.get('token'):
        userdatas = request.form.to_dict()
        username = userdatas.get('username', "")
        token = userdatas.get('token', "")
        userid = userdatas.get("userid", "")
        content = userdatas.get("content", "")
        kwargs = {"username": username, "token": token}
        data = setmyintroduction(userid,content,**kwargs)
        return json.dumps(data)
    else:
        return json.dumps({"code": "修改简介错误"})

# 修改密码
@app.route("/setpassword",methods=['POST'])
def setpassword():
    if request.method == 'POST' and request.form.get('userid') and request.form.get('password') and request.form.get('username') and request.form.get('token'):
        userdatas = request.form.to_dict()
        username = userdatas.get('username', "")
        token = userdatas.get('token', "")
        userid = userdatas.get("userid", "")
        password = userdatas.get("password", "")
        kwargs = {"username": username, "token": token}
        data = setmypassword(userid,password,**kwargs)
        return json.dumps(data)
    else:
        return json.dumps({"code": "修改密码错误"})

# 添加类型
@app.route("/addtype",methods=['POST'])
def addtype():
    if request.method == 'POST' and request.form.get('contenttype') and request.form.get('username') and request.form.get('token'):
        typedatas = request.form.to_dict()
        username = typedatas.get('username', "")
        token = typedatas.get('token', "")
        contenttype = typedatas.get('contenttype', "")
        kwargs = {"username": username, "token": token}
        data = addmytype(contenttype,**kwargs)
        return json.dumps(data)
    else:
        return json.dumps({"code": "添加类型错误"})

# 修改类型
@app.route("/settype",methods=['POST'])
def settype():
    if request.method == 'POST' and request.form.get('typeid') and request.form.get('contenttype') and request.form.get('username') and request.form.get('token'):
        typedatas = request.form.to_dict()
        username = typedatas.get('username', "")
        token = typedatas.get('token', "")
        contenttype = typedatas.get('contenttype', "")
        typeid = typedatas.get('typeid', "")
        kwargs = {"username": username, "token": token}
        data = setmytype(typeid,contenttype,**kwargs)
        return json.dumps(data)
    else:
        return json.dumps({"code": "添加类型错误"})

# 删除类型
@app.route("/deltype",methods=['POST'])
def deltype():
    if request.method == 'POST' and request.form.get('typeid') and request.form.get('username') and request.form.get('token'):
        typedatas = request.form.to_dict()
        username = typedatas.get('username', "")
        token = typedatas.get('token', "")
        typeid = typedatas.get('typeid', "")
        kwargs = {"username": username, "token": token}
        data = delmytype(typeid,**kwargs)
        return json.dumps(data)
    else:
        return json.dumps({"code": "删除类型错误"})

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True,threaded=True)
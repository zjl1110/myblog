# -*-coding:utf-8 -*-  
__author__ = "ZJL"


from sqlalchemy.sql import text
from .redis_manager import setTimeData,getData
import hashlib,time
#python3的html转义
import html

#python2的html转义
# import HTMLParser
# import cgi

from .mysql_manager import select_one_dict,select_all_dict,count_one,select_one,add_update_del

md5x = hashlib.md5()

# 获取个人信息
def getuserdata():
    dbkeys = ("id","username","userimg","userintroduction")
    data = select_one_dict("SELECT %s FROM %s ;" % ("id,username,headimg,introduce", "dbtest.user"), dbkeys)
    if data:
        print(data)
        return data
    else:
        return {"code":"个人信息数据获取错误"}

# 获取文章内容
def getcontent(contenttype,current,display):
    dbkeys = ("id","title","content","author","type")
    pagenum = str((int(current)-1)*int(display))
    if contenttype != "all":
        typedata = 'WHERE type="'+contenttype+'"'
    else:
        typedata = ""
    data = select_all_dict("SELECT %s FROM %s INNER JOIN %s ON %s INNER JOIN %s ON %s %s LIMIT %s,%s;"
                               % ("content.id,title,content,username,type", "content", "`user`",
                                  "content.userid=`user`.id", "contenttype", "content.typeid=contenttype.id", typedata,
                                  pagenum, display), dbkeys)
    if data:
        for d in data:
            print(d)
            #python3
            d["content"] = html.unescape(d["content"])
            # pyrhon2
            # d["content"] = HTMLParser.HTMLParser().unescape(d["content"])
            print("vvvvvvvvv",d)
        return data
    else:
        return {"code": "文章内容数据获取错误"}

# 获取文章总数总数
def getcontentcount(contenttype):
    if contenttype !="all":
        countdata = 'WHERE type="'+contenttype+'"'
    else:
        countdata = ""
    count = count_one(
        'SELECT COUNT(type) FROM content INNER JOIN contenttype ON content.typeid=contenttype.id %s' % (countdata))
    if count:
        return count
    else:
        return 0

# 获取文章类型
def getcontenttype():
    dbkeys = ("id","type")
    data = select_all_dict("SELECT `id`,`type` FROM `contenttype`", dbkeys)
    if data:
        print(data)
        return data
    else:
        return {"code":"文章分类错误"}

# 登入
def logindatadb(username,password):
    print("xxx",username,password)
    data = select_one(
        text("SELECT id FROM `user` WHERE `username`=:username AND `password` =:password ;").params(username=username,
                                                                                                    password=password))
    if data:
        print("11",data)
        return True
    else:
        print("22",data)
        return False

#登入后加入redis
def setlogintoken(key):
    value = key+str(time.time())
    md5x.update(value.encode(encoding='utf-8'))
    value = md5x.hexdigest()
    setTimeData(key,60*60*6,value)
    return value


# #登入验证
def usertoken(f):
    def wrapper_function(*args, **kwargs):
        username = kwargs.get("username","")
        token = kwargs.get("token","")
        if username and token:
            print("=========================")
            print(username)
            data = getData(username)
            if data == token:
                x = f(*args, **kwargs)
                x["login"]="1"
                return x
            else:
                return {"login":"0"}
        else:
            return {"login":"0"}
    return wrapper_function

#编辑文章db
def setcontent(conid,ctype,content,title,username):
    #python2的html转义
    # content = cgi.escape(content)
    # python3的html转义
    content = html.escape(content)
    if conid:
        updatasql = "UPDATE content SET content.title=\'%s\',content.content=\'%s\',content.typeid=(SELECT id FROM contenttype WHERE type=\'%s\') WHERE content.id=\'%s\';"%(title,content,ctype,conid)
        data = add_update_del(updatasql)
        print(data)
        return data
    else:
        usersql = "SELECT id FROM `user` WHERE username= \'%s\'"%(username)
        typesql = "SELECT id FROM `contenttype` WHERE type=\'%s\'"%(ctype)
        updatasql = "INSERT INTO content(title,content,typeid,userid) VALUES(\'%s\',\'%s\',(%s),(%s));"%(title,content,typesql,usersql)
        data = add_update_del(updatasql)
        print(data)
        return data

##编辑文章
@usertoken
def editmycontent(conid,ctype,content,title,**kwargs):
    username = kwargs.get("username", "")
    token = kwargs.get("token", "")
    data = setcontent(conid,ctype, content, title, username)
    if data:
        return {"code": "0"}
    else:
        return {"code": "编辑文章失败"}

#删除文章sql
def delcontents(conid):
    delsql = "DELETE FROM content WHERE id = \'%s\'"%(conid)
    data = add_update_del(delsql)
    print(data)
    return data

# 删除文章
@usertoken
def delmycontent(conid,**kwargs):
    data = delcontents(conid)
    if data:
        return {"code":"0"}
    else:
        return {"code":"删除文章失败"}

# 修改头像
def setheadimg(userid,imgurl):
    updataimgsql = "UPDATE user SET user.headimg=\'%s\' WHERE user.id=\'%s\';"%(imgurl,userid)
    data = add_update_del(updataimgsql)
    return data

# 修改简介
@usertoken
def setmyintroduction(userid,content,**kwargs):
    updatasql = "UPDATE user SET user.introduce=\'%s\' WHERE user.id=\'%s\';" % (content, userid)
    data = add_update_del(updatasql)
    if data:
        return {"code":"0"}
    else:
        return {"code":"修改简介错误"}

#修改密码
@usertoken
def setmypassword(userid,password,**kwargs):
    updatasql = "UPDATE user SET user.password=\'%s\' WHERE user.id=\'%s\';" % (password, userid)
    data = add_update_del(updatasql)
    if data:
        return {"code": "0"}
    else:
        return {"code": "修改密码错误"}

#添加类型
@usertoken
def addmytype(contenttype,**kwargs):
    querysql = "SELECT id FROM `contenttype` WHERE type= \'%s\'"%(contenttype)
    querydata = select_one(querysql)
    if querydata:
        return {"code":"类型已存在"}
    else:
        addsql = "INSERT INTO contenttype(type) VALUES(\'%s\');"%(contenttype)
        data = add_update_del(addsql)
        if data:
            return {"code":"0"}
        else:
            return {"code":"添加类型失败"}

#修改类型
@usertoken
def setmytype(typeid,contenttype,**kwargs):
    querysql = "SELECT id FROM `contenttype` WHERE type= \'%s\'" % (contenttype)
    querydata = select_one(querysql)
    if querydata:
        return {"code": "类型已存在"}
    else:
        addsql = "UPDATE contenttype SET type=\'%s\' WHERE id=\'%s\';" % (contenttype,typeid)
        data = add_update_del(addsql)
        if data:
            return {"code": "0"}
        else:
            return {"code": "修改类型失败"}

# 删除类型
@usertoken
def delmytype(typeid,**kwargs):
    querysql = "SELECT count(id) FROM `content` WHERE typeid= \'%s\'" % (typeid)
    querydata = select_one(querysql)
    if querydata[0]>0:
        return {"code": "此类型下有文章不可删除"}
    else:
        delsql = "DELETE FROM contenttype WHERE id = \'%s\'" % (typeid)
        data = add_update_del(delsql)
        if data:
            return {"code": "0"}
        else:
            return {"code": "删除类型失败"}


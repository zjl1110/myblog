# -*-coding:utf-8 -*-
__author__ = "ZJL"

import base64,os
from werkzeug.utils import secure_filename

def getpdf():
    with open("zjljl.pdf", "rb") as openpdf:
        base64_data = base64.b64encode(openpdf.read())
        pdfdata = {
            "pdfdata": "data:application/pdf;base64," + base64_data.decode('utf-8')
        }
        return pdfdata

def setpdf(file):
    # pdf格式
    ALLOWED_EXTENSIONS = set(['pdf'])
    # pdf存储目录
    UPLOAD_FOLDER = os.getcwd()
    filename = file.filename
    # 判断格式是否正确
    if file and ('.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS):
        filename = secure_filename(filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        return {"code":"0"}
    else:
        return {"code":"上传失败"}
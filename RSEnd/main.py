from flask import Flask, json, request, jsonify
from flask_cors import CORS
import pymysql
from flask import Flask, json, request, jsonify
from flask_cors import CORS
import pymysql
import cv2
import numpy as np
import os
DEBUG = True
from PIL import Image
from paddlers.deploy import Predictor
app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resource={r'/*': {'origins': '*'}})


@app.route('/adduser', methods=['get', 'post'])
def adduser():
    username = request.form.get("username")
    password = request.form.get("password")
    print(username)
    print(password)
    return "已接收用户信息"

@app.route('/uploadbefore', methods=['get', 'post'])
def uploadbefore():
    username = request.form.get("username")
    img = request.files['file']
    picname=img.filename
    file = img.read()

    file = cv2.imdecode(np.frombuffer(file, np.uint8), cv2.IMREAD_COLOR)  # 解码为ndarray
    imgfile1_path = "./static/images/"+username+"/A/"
    if not os.path.exists(imgfile1_path):
        os.makedirs(imgfile1_path)
    img1_path = os.path.join(imgfile1_path, picname)
    cv2.imwrite(filename=img1_path, img=file)
    url = "http://127.0.0.1:5000/static/images/"+username+"/A/" + picname
    print(url)
    picpath = "./static/images/" + username + "/A/" + picname

    tempmap = {"url": url,"picpath":picpath}
    return jsonify(tempmap)


predictor = Predictor("./models/rscd/", use_gpu=False)

@app.route('/uploadafter', methods=['get', 'post'])
def uploadafter():
    username = request.form.get("username")
    img = request.files['file']
    picname=img.filename
    file = img.read()

    file = cv2.imdecode(np.frombuffer(file, np.uint8), cv2.IMREAD_COLOR)  # 解码为ndarray
    imgfile1_path = "./static/images/"+username+"/B/"
    if not os.path.exists(imgfile1_path):
        os.makedirs(imgfile1_path)
    img1_path = os.path.join(imgfile1_path, picname)
    cv2.imwrite(filename=img1_path, img=file)
    url = "http://127.0.0.1:5000/static/images/"+username+"/B/" + picname
    print(url)
    picpath="./static/images/"+username+"/B/" + picname

    tempmap = {"url": url,"picpath":picpath}
    return jsonify(tempmap)

@app.route('/detectrscd', methods=['get', 'post'])
def detectrscd():
    username = request.form.get("username")

    # modelrscd.net.eval()
    fileA = request.form.get("imgA")
    fileB = request.form.get("imgB")
    print(fileA)
    print(fileB)

    res = predictor.predict((fileA, fileB))

    label_map = res['label_map']
    # 将numpy数组转换为PIL图像以便保存
    print(label_map)
    # 转换为二值图像：大于0.5的设置为255，否则为0
    binary_map = (label_map > 0.5).astype(np.uint8) * 255
    binary_image = Image.fromarray(binary_map)
    # 保存二值图像到本地，这里以'binary_image.png'为例，您可以自行修改文件名
    picname=fileA.split('/')[-1]
    outpath = "./static/images/" + username + "/res/"
    if not os.path.exists(outpath):
        os.makedirs(outpath)
    outpic = "./static/images/" + username + "/res/" + picname
    binary_image.save(outpic)
    print("二值图像已成功保存至本地。")
    url = "http://127.0.0.1:5000/static/images/" + username + "/res/" + picname
    tempmap = {"url": url}
    return jsonify(tempmap)



if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
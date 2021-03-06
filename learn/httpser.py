# coding:utf-8
import json

from flask import Flask, request
import text_process

# punkt not found
# 1.到github https://github.com/nltk/nltk_data 把package文件下载下来，
# 2.把packages文件夹拷贝到报错显示的搜索路径
# 3.解压对应文件，如：punkt.zip


app = Flask(__name__)

MY_URL = '/knowledge/api/v1/'

# hello = '今天天气真好呀'
# not_hello = '为什么今天天气不好呀'
# keystr="服务器上架"
# topN=3


# get
@app.route(MY_URL + 'get/tasks', methods=['GET'])
def get_task():
    param = request.args.to_dict()
    # print(param)  # request.args请求参数
    # print(type(param))
    # print(param)
    keystr = param['keystr']
    topN = param['topN']

    # return str(text_process.handle_client("工单主题:核心系统数据库服务器上架;", 3))
    # in_json = json.dumps(text_process.handle_client("工单主题:核心系统数据库服务器上架;", 3))
    # return str(in_json)
    # print(text_process.handle_client("工单主题:核心系统数据库服务器上架;", 3))
    nameDict = {"1": keystr, "2": topN}
    return str(nameDict)


# post
@app.route(MY_URL + 'post/tasks', methods=['POST'])
def post_task():
    param = request.json
    print(param)  # request.args请求参数
    # print(type(param))
    # print(param)
    keystr = param['keystr']
    topN = param['topN']

    # return str(text_proprint(text_process.handle_client("工单主题:核心系统数据库服务器上架;", 3))cess.handle_client("工单主题:核心系统数据库服务器上架;", 3))
    #
    # in_json = json.dumps(text_process.handle_client(keystr, topN))
    #return str(in_json)

    nameDict = {"1": keystr, "2": topN}
    return str(nameDict)

@app.route(MY_URL + 'add', methods=['GET'])
def add_record():
    param = request.args.to_dict()
    # print(param)  # request.args请求参数
    # print(type(param))
    # print(param)
    keystr = param['keystr']
    topN = param['topN']
    nameDict = {"1": keystr, "2": topN}
    return str(nameDict)


if __name__ == '__main__':
    # app.run(debug=True, host='0.0.0.0', port=8000)
    app.run(debug=True, port=8000)
# http://127.0.0.1:5000/knowledge/api/v1/get/tasks?keystr="服务器上架"&topN=3
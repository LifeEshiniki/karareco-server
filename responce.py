import json
import bottle
import subprocess
import sys
import os
import time
import socket
from bottle import request,response,template,redirect
from bottle import route,HTTPError
from bottle import get,post,run


@route('/')
def root():
    return template("hello {{string}}\n"
                    '<a href="./upload">upload</a>', string = "world")
# クライアントから音声ファイルを受け取る
@route('/upload', method='POST')
def upload():
    upload = request.files.get('upload')

    upload.save("/tmp",overwrite=True)
    return template('{{string}} is uploaded.\n', string = upload.filename) # check


    # クライアントから送られた音声ファイルをHoundifyに認識させる
    '''
    (⊃|⊂) → (⊃*⊂)
    ケツマンおっぴろげてメールを待つ
    '''

    # houndifyからのJSONをダンプ
    result = '{"otintin":"biroooon","samurai":"shakiiin","tintinzamurai":"tintinzamurai" }'
    # houndifyから送信されたJSONをresultに代入する予定

    dec = json.loads(result)

    res_data = {"Result":dec["otintin"],"song":dec["samurai"],"artist":dec["tintinzamurai"],"album":dec["tintinzamurai"]}


    # クライアントにJSON形式で結果を送信

    res = json.dumps(res_data)
    response.status = 200
    response.content_type = "application/json"
    return res


# サーバを立ち上げ
if __name__ =='__main__':
    run(host="localhost", port=8080,
        debug=True, reloader=True)

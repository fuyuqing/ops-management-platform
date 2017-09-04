#_*_coding:utf-8_*_

from flask import Flask,request
from host_get import Host_get

app = Flask(__name__)
data = Host_get.getHostItem()

@app.route('/')
def index():
    return data
@app.route("/metrics/find/")
def metrics():
    if request.args.get('query') == '*':
        return data

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=11111,debug=True)
from flask import Blueprint, request

nn = Blueprint("nn", __name__, url_prefix="/nn")

# 定义一个settimeout api
import threading
def setTimeout(cb,delay,*args):
    threading.Timer(delay,cb,args).start()

@nn.route('/', methods=['GET', 'POST'])
def index():
    return {"msg":"nn接口正常"}
#查询所有数据


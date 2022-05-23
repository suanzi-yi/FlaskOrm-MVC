from flask import Blueprint, request
from startapp.model.baseModel import db
from startapp.service.userService import create_user, insert_one, get_all
from startapp.model.userModel import UserModel
from  startapp.model.jobModel import JobModel
from startapp.util.scrapyNBA import task1,task2,task3,task4
user = Blueprint("user", __name__, url_prefix="/user")

# 定义一个settimeout api
import threading
def setTimeout(cb,delay,*args):
    threading.Timer(delay,cb,args).start()

@user.route('/', methods=['GET', 'POST'])
def index():
    return {"msg":"接口正常"}

#删除表，并创建
@user.route('/createtable', methods=['GET', 'POST'])
def createtable():
    status = create_user()
    return {
        "status": status,
        "msg": "重新创建表成功"
    }

#插入数据
@user.route('/insertone', methods=['GET', 'POST'])
def insertone():
    username = request.values.get("username")
    password = request.values.get("password")
    model = UserModel(username=username, password=password)
    status = insert_one(model)
    return {
        "status": status,
        "msg": "插入成功"
    }

#查询所有数据
@user.route('/getall', methods=['GET', 'POST'])
def getall():
    return {
        "status": 200,
        "msg": "查询成功",
        # "data": get_all(UserModel)
        "data": repr(get_all(UserModel))
    }

# 插入爬虫任务
@user.route('/addjob', methods=['GET', 'POST'])
def addjob():
    data=request.get_json()
    # username=data["username"]
    url=data["url"]
    uuid=data["uuid"]
    job = JobModel(username='admin', uuid=uuid,url=url,status='1')
    try:
        db.session.add(job)
        db.session.commit()
        status=1
    except:
        status=-1
    # 先返回值，然后等3s再启动任务
    # setTimeout()
    return {
        "data":data,
        "status": status,
        "msg": "插入成功"
    }

@user.route('/getjob', methods=['GET', 'POST'])
def getjob():
    job = JobModel()
    job.query.all()
    return {
        "data": repr(job.query.all()),
        "status": 1,
        "msg": "查询成功"
    }
@user.route('/getalldata', methods=['GET', 'POST'])
def getalldata():
    data=task4()
    return {
        "data": data,
        "status": 1,
        "msg": "查询成功"
    }
#三大位置能力折线图参数[[],[],[],[]]
@user.route('/threeability', methods=['GET', 'POST'])
def threeability():
    data=task1()
    return {
        "data":data,
        "status": 1,
        "msg": "查询成功"
    }
#个人能力归一化图，参数name [{},{},{},{}]
@user.route('/onedata', methods=['GET', 'POST'])
def onedata():
    name = request.values.get("name")
    data=task2(name)
    return {
        "data":data,
        "status": 1,
        "msg": "查询成功"
    }
#top5堆积图 [[],[],[]]
@user.route('/top5', methods=['GET', 'POST'])
def top5():
    data=task3()
    return {
        "data":data,
        "status": 1,
        "msg": "查询成功"
    }
from flask import Blueprint, request
from startapp.model.baseModel import db
from startapp.model.jobModel import JobModel
from startapp.util.scrapyNBA import task1,task2,task3,task4
scrapy = Blueprint("scrapy", __name__, url_prefix="/scrapy")

# 定义一个settimeout api
import threading
def setTimeout(cb,delay,*args):
    threading.Timer(delay,cb,args).start()

@scrapy.route('/', methods=['GET', 'POST'])
def index():
    return {"msg":"scrapy接口正常"}

# 插入爬虫任务
@scrapy.route('/addjob', methods=['GET', 'POST'])
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

@scrapy.route('/getjob', methods=['GET', 'POST'])
def getjob():
    job = JobModel()
    job.query.all()
    return {
        "data": repr(job.query.all()),
        "status": 1,
        "msg": "查询成功"
    }
@scrapy.route('/getalldata', methods=['GET', 'POST'])
def getalldata():
    data=task4()
    return {
        "data": data,
        "status": 1,
        "msg": "查询成功"
    }
#三大位置能力折线图参数[[],[],[],[]]
@scrapy.route('/threeability', methods=['GET', 'POST'])
def threeability():
    data=task1()
    return {
        "data":data,
        "status": 1,
        "msg": "查询成功"
    }
#个人能力归一化图，参数name [{},{},{},{}]
@scrapy.route('/onedata', methods=['GET', 'POST'])
def onedata():
    name = request.values.get("name")
    data=task2(name)
    return {
        "data":data,
        "status": 1,
        "msg": "查询成功"
    }
#top5堆积图 [[],[],[]]
@scrapy.route('/top5', methods=['GET', 'POST'])
def top5():
    data=task3()
    return {
        "data":data,
        "status": 1,
        "msg": "查询成功"
    }
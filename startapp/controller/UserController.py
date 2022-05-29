from flask import Blueprint, request
from startapp.service.userService import create_user, insert_one, get_all
from startapp.model.userModel import UserModel

user = Blueprint("user", __name__, url_prefix="/user")

@user.route('/', methods=['GET', 'POST'])
def index():
    return {"msg":"user接口正常"}

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
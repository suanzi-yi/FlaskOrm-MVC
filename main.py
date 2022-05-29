from flask import Flask
from flask_cors import CORS
from startapp.controller.UserController import user
from  startapp.controller.NnController import nn
from startapp.controller.ScrapyController import scrapy
from startapp.model.baseModel import db

app = Flask(__name__)
CORS(app)
# 相关配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:3306/flaskorm'  # 用户名：密码@mysql地址/数据库
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db.init_app(app)

if __name__ == '__main__':
    app.register_blueprint(user)
    app.register_blueprint(nn)
    app.register_blueprint(scrapy)
    app.run(host='127.0.0.1', port=80)

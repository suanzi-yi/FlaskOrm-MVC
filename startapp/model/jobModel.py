# -*- coding: utf-8 -*-
# @Time : 2022/5/21 17:25
# @Author : suanzi
# @Site : 
# @File : jobModel.py.py
# @Software: PyCharm
from startapp.model.baseModel import db
class JobModel(db.Model):
    #表
    __tablename__ = 'job'
    #字段
    id = db.Column(db.Integer, primary_key=True)  # 设置主键, 默认自增
    username = db.Column('username', db.String(20))  # 设置字段名 和 唯一约束
    uuid= db.Column( db.String(50))#
    url = db.Column( db.String(50))  # 设置默认值约束 和 索引
    status= db.Column( db.String(20))
    #tostring函数，能将模型打印出来，数组
    def __repr__(self):
        return str({"id":self.id,"username":self.username,"uuid":self.uuid,"url":self.url,"status":self.status})
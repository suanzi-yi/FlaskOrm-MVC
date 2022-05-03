from startapp.model.baseModel import db
class UserModel(db.Model):
    #表
    __tablename__ = 'user'
    #字段
    id = db.Column(db.Integer, primary_key=True)  # 设置主键, 默认自增
    username = db.Column('username', db.String(20), unique=True)  # 设置字段名 和 唯一约束
    password = db.Column(db.Integer)  # 设置默认值约束 和 索引
    #tostring函数，能将模型打印出来，数组
    def __repr__(self):
        return str({"id":self.id,"username":self.username,"password":self.password})
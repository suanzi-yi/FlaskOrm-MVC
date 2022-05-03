在main.py配置用户名和密码  
在mysql创建flaskorm数据库  
启动main.py 访问http://127.0.0.1/user/createtable 则自动创建表
#运行环境
python
###依赖：
requirements.txt
###数据库配置:
mysql  
用户名：root  
密码：root  
数据库：flaskorm
#项目架构
###startapp
###--controller 控制层
####----Home.py 路由与视图函数
###--service 服务层
####----userService.py 服务函数
###--repository 持久层
####----userDao.py 持久化函数
###--model 模型层

#运行原理
###遵循MVC设计模式  
client发送请求==》  
==》controller层接受到请求，提取参数，封装成一个model  
==>将封装好的model发送到service层，在service层完成所需操作  
==》再发送到repository层持久化，在数据库中保存
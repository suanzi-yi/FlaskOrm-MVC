#项目根地址：
http://127.0.0.1/user
###接口状态测试：
####地址：
'/'
####响应:  
{
	"msg": "接口正常"
}
###获取所有数据：
接口地址：
'/getall'
####响应：
{
	"data": "[{'id': 1, 'username': '111', 'password': 222}, {'id': 2, 'username': 'zjx', 'password': 123}]",
	"msg": "查询成功",
	"status": 200
}
###插入用户：
####地址：
'/insertone'
####参数：
username 非空   
password 非空
####方法：
get，post  
响应：  
{
	"msg": "插入成功",
	"status": 1
}

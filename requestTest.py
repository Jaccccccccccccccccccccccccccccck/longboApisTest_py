import requests
import re
from bs4 import BeautifulSoup

#保持session
s = requests.Session()
#获取登陆界面的_csrf值
response = s.get("http://180.153.108.40:8080/longboApis/login")
bs=BeautifulSoup(response.text,"html.parser")
_csrf_body = bs.find(attrs={'name':re.compile('_csrf')});
_csrf = (_csrf_body.get("value"))
#登陆,此处的user，user为登陆账号和密码
login_params={'username':'user','password':'user','_csrf':_csrf}
s.post("http://180.153.108.40:8080/longboApis/login",params=login_params)
#请求测试 JL_BASE_1102为请求的表名，1为页码，100为页数大小
response = s.get("http://180.153.108.40:8080/longboApis/jlzx/JL_BASE_1102/1/100")
print(response.text)



